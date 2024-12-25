from rest_framework import serializers
from . models import Product, Category, Review
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # added_by = UserSerializer()
    # bought_by = UserSerializer(allow_null=True)
    # categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'image',
            'description',
            'price',
            'added_by',
            'bought_by',
            'categories',
        ]