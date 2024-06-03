from django.shortcuts import render, get_object_or_404, redirect
from backend . models import Category, Brand, Product
from frntnd . models import Useraccount, Cart, Register
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from django.utils import timezone
import random
import smtplib
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


# Create your views here.  

def home(request):
    cate = Category.objects.all()
    brand = Brand.objects.all()
    pro = Product.objects.all()
    register = Register.objects.all()
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
        account = Useraccount(name=name, phone=phone, state=state, city=city, address=address, pin=pin)
        account.save()
    accounts = Useraccount.objects.all()
    return render(request, 'account.html', {'accounts': accounts})

def editaccout(request):
    acc = Useraccount.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        pin = request.POST.get('pin')

        acc.name = name
        acc.phone = phone
        acc.state = state
        acc.city = city
        acc.address = address
        acc.pin = pin
        acc.save()
        return redirect('account')
    return render(request, 'account.html', {'acc': acc})


def deleteaccount(request, id):
    accound = Useraccount.objects.get(id=id)
    accound.delete()
    return render(request, 'account.html')


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

#  Login views  

def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        passwrd = request.POST.get('password')
        register = Register(username=uname, password=passwrd, email=email)
        register.save()
    return render(request, 'product.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        passwrd = request.POST.get('password')

        if Register.objects.filter(email=email, password=passwrd).exists():
            request.session['email']=email 
            request.session['password']=passwrd 
            return redirect(home) 
        else:
            message = "Your username and password doesn't match :("
            return render(request, 'login.html', {'message': message}) 
    return render(request, 'login.html') 


def logout(request):
    username=request.session['username']
    del request.session['password']
    username.delete()
    return render(request, 'home.html', {'username': username})


#  OTP views



def simple_mail(request):
    send_mail(
        subject='OTP for login',
        message='otp sender',
        from_email="darshuuu11@gmail.com",
        recipient_list=['darshuuu11@gmail.com'])
    return HttpResponse("otp messageee")


def otpgenerate(request):
    if request.method == 'POST':
       mailid = request.POST.get('email')

    
    # Validate the email
    try:
        validate_email(mailid)
        valid_email = True
    except ValidationError:
        valid_email = False
        

        otp = random.randint(100000, 999999)
        print("otp code is", otp)
        request.session['otp_code'] = otp
        request.session['created_at'] = timezone() 
        request.session['email'] = mailid   


#  send otp in mail 
        send_mail(
            subject='otp for Login ',
            message=f'Your otp {otp}',
            from_email="darshuuu11@gmail.com",
            recipient_list=['darshuuu11@gmail.com'])
        return redirect('home')
    return render(request,'otpgenerate.html')




def otpvalidate(request):
    if request.method == 'POST':
        input_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        otp_timestamp = request.session.get('otp_timestamp')
        current_timestamp = timezone.now().timestamp()

         # Set OTP validity period to 15 seconds
        otp_validity_period = 15  # 15 seconds

        if stored_otp and otp_timestamp and (current_timestamp - otp_timestamp) <= otp_validity_period:
            if str(input_otp) == str(stored_otp):
                return HttpResponse("OTP is valid")
            else:
                return HttpResponse("Invalid OTP")
        else:
            return HttpResponse("OTP has expired or is invalid")
        
        