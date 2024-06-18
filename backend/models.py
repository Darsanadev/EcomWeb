from django.db import models

# Create your models here.  

class Category(models.Model):
    cname = models.CharField(max_length=100,null=True,  blank=True)             
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='media', null=True)
    is_listed = models.BooleanField(default=True, null=True, blank=True)
    


class Brand(models.Model):
    brand = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    is_listed = models.BooleanField(default=True,null=True, blank=True)
    offer = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.brand

class Product(models.Model):    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)   
    product = models.CharField(max_length=200,null=True, blank=True)    
    size = models.IntegerField(null=True, blank=True)   
    landing_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)     
    selling_price = models.IntegerField(null=True, blank=True)  
    description = models.TextField(null=True, blank=True) 
    image = models.ImageField(upload_to='media', null=True, blank=True)
    image1 = models.ImageField(upload_to='media', null=True, blank=True)
    image2 = models.ImageField(upload_to='media', null=True, blank=True)
    image3 = models.ImageField(upload_to='media', null=True, blank=True)
    is_listed = models.BooleanField(default=True, null=True, blank=True)   

