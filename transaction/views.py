from django.shortcuts import render
from rest_framework.views import APIView
from . models import Transaction
from . serializers import TransactionSerializer, ProductBuySerializer
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