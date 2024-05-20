from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=199, blank=True, null=True, unique=True)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    description = models.TextField()
    price = models.IntegerField()
    categories = models.ManyToManyField(Category, related_name='categories')
    added_by = models.ForeignKey(User, related_name='added_by', on_delete=models.CASCADE, blank=True, null=True)
    bought_by = models.ForeignKey(User, related_name='bought_by', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self) -> str:
        return f'Products name : {self.name}'
    
class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.SET_NULL, null=True, blank=True)
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'Review by : {self.user.username}'
