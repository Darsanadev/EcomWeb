from django.db import models
from backend.models import Product
# from django.contrib.auth.models import AbstractUser

# Create your models here.

class Useraccount(models.Model):
    name = models.CharField(max_length=100,null=True,  blank=True)
    phone = models.BigIntegerField(blank=True, null=False, default=True)
    state = models.CharField(max_length=200, blank=False, default=True)
    city = models.CharField(max_length=200, null=False, default=True)
    address = models.TextField(null=True, blank=True)
    pin = models.IntegerField(null=True, blank=True)
    

class Register(models.Model):
    username = models.CharField(max_length=100,null=False, default=True)
    email = models.EmailField(null=False, default=True)
    password = models.CharField(max_length=100, null=False, default=True)
    phone = models.IntegerField(null=True)
    otpcode = models.IntegerField(null=True, blank=True)
    

class Cart(models.Model):  
    prodt = models.ForeignKey(Product, on_delete=models.CASCADE, default=1) 
    user = models.ForeignKey(Useraccount, on_delete=models.CASCADE) 
    orderdate = models.DateTimeField(auto_now_add=True) 
    quantity = models.PositiveIntegerField(default=1) 
    price = models.IntegerField(blank=True, default=1) 
    total = models.IntegerField(null=True, blank=True, default=1) 
    
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICES = ((ORDER_PROCESSED, "ORDER_PROCESSED"),
                      (ORDER_DELIVERED, "ORDER_DELIVERED"),
                      (ORDER_REJECTED, "ORDER_REJECTED"))
    order_status = models.IntegerField(choices=STATUS_CHOICES, default=CART_STAGE)
