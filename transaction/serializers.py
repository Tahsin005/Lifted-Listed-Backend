from rest_framework import serializers
from . models import Transaction
from account.models import UserAccount
from product.models import Product
from . constants import TRANSACTION_TYPE
from django.db import transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['account', 'amount']
        read_only_fields = ['balance_after_transaction', 'transaction_type']

    def validate_account(self, value):
        try:
            UserAccount.objects.get(id=value.id)
        except UserAccount.DoesNotExist:
            raise serializers.ValidationError({'error': 'Account does not exist'})
        return value

    def validate_amount(self, value):
        min_deposit_amount = 100
        if value >= min_deposit_amount:
            return value
        else:
            raise serializers.ValidationError(f'Minimum deposit amount is {min_deposit_amount}')

    def create(self, validated_data):
        account = validated_data['account']
        amount = validated_data['amount']
        current_balance = account.balance
        new_balance = current_balance + amount

        account.balance = new_balance
        validated_data['transaction_type'] = 'Deposit'
        account.save()
        transaction = Transaction.objects.create(
            account=account,
            amount=amount,
            balance_after_transaction=new_balance,
            transaction_type='Deposit'
        )
        return transaction

class ProductBuySerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    seller_id = serializers.IntegerField()  # Assuming seller_id is defined in the Product model

    def validate(self, data):
        product_id = data.get('product_id')
        user_id = data.get('user_id')
        seller_id = data.get('seller_id')

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError({'error': 'Product does not exist'})

        if product.bought_by:
            raise serializers.ValidationError({'error': 'Product has already been bought'})

        try:
            user_account = UserAccount.objects.get(user_id=user_id)
        except UserAccount.DoesNotExist:
            raise serializers.ValidationError({'error': 'User does not exist'})

        if user_account.balance < product.price:
            raise serializers.ValidationError({'error': 'Insufficient balance'})

        data['product'] = product
        data['user_account'] = user_account
        data['seller_id'] = seller_id
        return data

    def save(self):
        product = self.validated_data['product']
        user_account = self.validated_data['user_account']
        seller_id = self.validated_data['seller_id']
        seller_full_account = UserAccount.objects.get(user__id=seller_id)
        buying_cost = product.price

        with transaction.atomic():
            product.bought_by_id = user_account.user_id
            product.save()

            user_account.balance -= buying_cost
            user_account.save(update_fields=['balance'])

            Transaction.objects.create(
                account=user_account,
                amount=buying_cost,
                balance_after_transaction=user_account.balance,
                transaction_type='Pay'
            )

            seller_full_account.balance += buying_cost
            seller_full_account.save(update_fields=['balance'])

            Transaction.objects.create(
                account=seller_full_account,
                amount=buying_cost,
                balance_after_transaction=seller_full_account.balance,
                transaction_type='Receive'
            )

        return product

class UserTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['amount', 'balance_after_transaction', 'transaction_type', 'timestamp']