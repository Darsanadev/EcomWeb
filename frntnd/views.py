from django.shortcuts import render, get_object_or_404, redirect
from backend . models import Category, Brand, Product
from frntnd . models import Account, Cart, Login
from django.contrib import messages

# Create your views here.  

def home(request):
    cate = Category.objects.all()
    brand = Brand.objects.all()
    pro = Product.objects.all()
    register = Login.objects.all()
    return render(request, 'home.html', {'cate': cate, 'brand': brand, 'pro': pro, 'register':register})


def product(request):
    cate = Category.objects.all()
    brand = Brand.objects.all()
    pro = Product.objects.all()
    return render(request, 'product.html', {'cate': cate, 'brand': brand, 'pro': pro})


def category(request, catname):
    cate = Category.objects.all()
    brand = Brand.objects.all()
      # Filter products based on category name (assuming Category has 'cname' field)
    category = get_object_or_404(Category, cname=catname)
    # brands = get_object_or_404(Brand, brand=brandname)
    pro = Product.objects.filter(category=category)

    context = {
        'cate': cate,
        'brand': brand,
        'pro': pro,
    }
    return render(request, 'category.html', context) 


def singleproduct(request, id):
    cate = Category.objects.all()
    brand = Brand.objects.all()
    pro = Product.objects.filter(id=id) 
     
    return render(request, 'singleproduct.html', {'cate': cate, 'brand': brand, 'pro': pro})

# Change Employee.objects.get(id=id) to Employee.objects.filter(id=id)

# "filter() will always give you a QuerySet" - it's iterable

# get() - return single object and it's not iterable


def account(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        pin = request.POST.get('pin')
        account = Account(name=name, phone=phone, state=state, city=city, address=address, pin=pin)
        account.save()
    accounts = Account.objects.all()
    return render(request, 'account.html', {'accounts': accounts})

def edi_accout(request):
    acc = Account.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        pin = request.POST.get('pin')

        acc.name=name
        acc.phone=phone
        acc.state=state
        acc.city=city
        acc.address=address
        acc.pin=pin
        acc.save()
        return redirect('account')

    return render(request, 'account.html', {'acc':acc})

def deleteaccount(id):
    accound = Account.objects.get(id=id)
    accound.delete()
    return redirect('account')


def cartdata(request):
    if request.method == 'POST':
        image = request.POST.get('image')
        user = request.POST.get('user')
        orderdate = request.POST.get('orderdate')
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        total = request.POST.get('total')
        cartt = Cart(image=image, user=user, orderdate=orderdate, product=product, quantity=quantity, price=price, total=total)
        cartt.save()
        return redirect(cart)
        
    return render(request, 'cartdata.html')
    


def cart(request, id):
    product = Product.objects.get(id=id)
    category = Category.objects.all()
    brand = Brand.objects.all()
    cartt = Cart.objects.get(id=id)
    return render(request, 'cart.html', {'product': product, 'category': category, 'brand': brand, 'cartt': cartt})


def removecart(request, id):
    cartt = Cart.objects.get(id=id)
    cartt.delete()
    return render(request, 'cart.html', {'cartt': cartt})


def checkout(request):
    return render(request, 'checkout.html')


def contact(request):
    return render(request, 'contact.html')


def whishlist(request):
    return render(request, 'whishlist.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        passwrd = request.POST.get('password')
        register = Login(username=uname, password=passwrd, email=email)
        register.save()
        if Login.objects.filter(username=uname, password=passwrd).exists():
            request.session['username']=uname
            request.session['password']=passwrd
            return render(request, 'home.html')
        else:
            message="Your username and password doesn't match :( "
            return render(request, 'login.html', {'message': message}) 
    return render(request, 'login.html') 

def logout(request):
    username=request.session['username']
    username.delete()
    return render(request, 'home.html', {'username': username})
