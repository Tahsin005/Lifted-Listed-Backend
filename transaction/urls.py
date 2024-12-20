from django.urls import path
from . import views

urlpatterns = [
    path('deposit/', views.TransactionAPIView.as_view(), name='deposit'),
    path('transactions/<int:user_id>/', views.UserTransactionsAPIView.as_view(), name='user-transactions'),
]