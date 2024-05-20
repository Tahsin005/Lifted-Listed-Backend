from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 

rounter = DefaultRouter()
rounter.register('list', views.ProductViewSet)
rounter.register('category', views.CategoryViewSet)
rounter.register('review', views.ReviewViewSet)

urlpatterns = [
    path('', include(rounter.urls)),
]

