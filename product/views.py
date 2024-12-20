from django.shortcuts import render
from rest_framework import viewsets
from . models import Product, Category, Review
from . serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name', 'categories__name', 'categories__slug']

    def get_queryset(self):
        queryset = super().get_queryset()
        categories = self.request.query_params.getlist('categories__slug', None)
        max_price = self.request.query_params.get('max_price', None)

        if categories:
            queryset = queryset.filter(categories__slug__in=categories)

        if max_price:
            try:
                max_price = int(max_price)
                queryset = queryset.filter(price__lte=max_price)
            except ValueError:
                pass

        return queryset.distinct()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product__id']

class ProductsBoughtByUserAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(bought_by=self.request.user)


class ProductsAddedByUserAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(added_by=self.request.user)
