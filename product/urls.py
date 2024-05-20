from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 
from transaction import views as transaction_views
rounter = DefaultRouter()
rounter.register('list', views.ProductViewSet)
rounter.register('category', views.CategoryViewSet)
rounter.register('review', views.ReviewViewSet)

urlpatterns = [
    path('', include(rounter.urls)),
    path('buy/', transaction_views.ProductBuyAPIView.as_view(), name='buy'),
]

