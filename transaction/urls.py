from django.urls import path
from . import views

urlpatterns = [
    path('deposit/', views.TransactionAPIView.as_view(), name='deposit'),
]
