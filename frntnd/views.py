from django.shortcuts import render
from backend . models import Category, Brand, Product

# Create your views here.  

def home(request):
    cate = Category.objects.all()
    brand = Brand.objects.all()
    pro = Product.objects.all()
    return render(request, 'home.html', {'cate': cate, 'brand': brand, 'pro': pro})


def product(request):
    cate = Category.objects.all()
    brand = Brand.objects.all()
    pro = Product.objects.all()
    return render(request, 'product.html', {'cate': cate, 'brand': brand, 'pro': pro})


def category(request, catname):
    cate = Category.objects.all()
    brand = Brand.objects.all()
    pro = Product.objects.filter(cname=catname) 
    return render(request, 'category.html', {'cate': cate, 'brand': brand, 'pro': pro})


def singleproduct(request):
    cate = Category.objects.all()
    brand = Brand.objects.all()
    pro = Product.objects.all()
    return render(request, 'singleproduct.html', {'cate': cate, 'brand': brand, 'pro': pro})


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def account(request):
    return render(request, 'account.html')


def contact(request):
    return render(request, 'contact.html')


def whishlist(request):
    return render(request, 'whishlist.html')
