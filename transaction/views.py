from django.shortcuts import render
from rest_framework.views import APIView
from . models import Transaction
from . serializers import TransactionSerializer, ProductBuySerializer, UserTransactionSerializer
from account.models import UserAccount
from rest_framework.response import Response
# Create your views here.

class TransactionAPIView(APIView):
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            transaction = serializer.save()
            response_data = {
                'message' : 'Deposit successfull',
                'transaction_id' : transaction.id
            }

            return Response(response_data)
        else:
            return Response(serializer.errors)

class ProductBuyAPIView(APIView):
    def post(self, request):
        serializer = ProductBuySerializer(data=request.data)
        if serializer.is_valid():
            bought_product = serializer.save()

            return Response({'message': 'You have successfully bought the product {bought_product.name}'})
        return Response(serializer.errors)

class UserTransactionsAPIView(APIView):
    def get(self, request, user_id):
        try:
            user_account = UserAccount.objects.get(user_id=user_id)
        except UserAccount.DoesNotExist:
            return Response({'error': 'User account does not exist'})

        transactions = Transaction.objects.filter(account=user_account)
        serializer = UserTransactionSerializer(transactions, many=True)
        return Response(serializer.data)