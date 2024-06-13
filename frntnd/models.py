from django.db import models

# Create your models here.

class Useraccount(models.Model):
    name = models.CharField(max_length=100,null=True,  blank=True)
    phone = models.BigIntegerField(blank=True)
    state = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=200, null=False)
    address = models.TextField(null=True, blank=True)
    pin = models.IntegerField(null=True, blank=True)


class Cart(models.Model):
    image = models.ImageField(upload_to='media', null=True, blank=True)
    user = models.CharField(max_length=200, blank=True)
    orderdate = models.DateTimeField(auto_now_add=True)
    product = models.CharField(max_length=200, blank=True)
    quantity = models.PositiveIntegerField()
    price = models.IntegerField(blank=True)
    total = models.IntegerField(null=True, blank=True)


class Register(models.Model):
    username = models.CharField(max_length=100,null=False, default=True)
    email = models.EmailField(null=False, default=True)
    password = models.CharField(max_length=100, null=False, default=True)
    phone = models.IntegerField(null=False)
    otpcode = models.IntegerField(null=True, blank=True)


# class OTP(models.Model):
#     username = models.ForeignKey(Register, on_delete=models.CASCADE)
#     otp_code = models.CharField(max_length=6)
#     otpcreate_time = models.DateTimeField(auto_now_add=True)
#     email = models.EmailField(null=True, blank=True)

