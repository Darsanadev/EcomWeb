from django.shortcuts import render, get_object_or_404, redirect
from backend . models import Category, Brand, Product
from frntnd . models import Useraccount, Cart, Register
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
import random
from datetime import datetime, timedelta
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
    pro = Product.objects.filter(id=id) 
    return render(request, 'singleproduct.html', {'pro': pro})

# Change Employee.objects.get(id=id) to Employee.objects.filter(id=id)

# "filter() will always give you a QuerySet" - it's iterable
# get() - return single object and it's not iterable


# Login views  


def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        passwrd = request.POST.get('password')
        register = Register(username=uname, password=passwrd, email=email)
        register.save()
    return render(request, 'register.html')


def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        userlogin = Register.objects.filter(username = username, password = password).exists()

        if userlogin:
            request.session['username'] = username
            request.session['password'] = password
            
            # message "Good Job Succescc logn"
            return redirect('frntnd:home')
        else:
            return HttpResponse("its wromng")
    return render(request, 'userlogin.html')            


def logout(request):
    del request.session['username']
    del request.session['password']
    return HttpResponse("Byee the bye :) ")


def forgotpass(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = Register.objects.filter(email=email)

        request.session['regemail'] = email

        if user.exists():
            link = "http://127.0.0.1:8000/frntnd/newpassword/"
            
            send_mail(
                subject='Reset Your Password ',
                message=f' Hey Your reset password link  {link}  click the link to reset password',
                from_email="darshuuu11@gmail.com",
                recipient_list=[email])
        
        else:
            return redirect( 'frntnd:forgotpassword')
        
    return render(request, 'forgotpassword.html') 
   

def newpassword(request):
    if request.method=='POST':
        email = request.session.get('regemail')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            user = Register.objects.get(email=email)
            user.password=password1
            user.save()
            return redirect('frntnd:userlogin')
        
        else:
            # msgs "password Doesn't match"
            return redirect('frntnd:newpassword')
            
    return render(request, 'newpassword.html')


def otpgenerate(request):   
    if request.method == 'POST':
       mailid = request.POST.get('email')

       # Validate the email
       try:
        validate_email(mailid)
        valid_email = True
       except ValidationError:
            valid_email = False  

       if valid_email:
            otp = random.randint(100000, 999999)
            otptime = datetime.now()
            print("otppp", otp)

            # Convert datetime to string
            otptime_str = otptime.isoformat()
            
            # session are Used for temporary, fast-access storage of data 
            request.session['storedotp'] = otp   
            request.session['otpcreate_time'] = otptime_str 
            request.session['email'] = mailid  
             
            send_mail(
                subject='otp for Login ',
                message=f' Hey Your OTP :  {otp} enjoyy hav a gud day',
                from_email="darshuuu11@gmail.com",
                recipient_list=[mailid])
           
            return redirect('frntnd:otpvalidate')
    return render( request, 'otpgenerate.html')     


def otpvalidate(request):
    if request.method == 'POST':
        inputotp = request.POST.get('inpotp')
        storedotp = request.session.get('storedotp')
        
        print(f"Storeeeee OTP: {storedotp}")
        print(f"Inputeee OTP: {inputotp}")

        if str(inputotp) == str(storedotp):
            # Clear session data if needed  
            # del request.session['storedotp']  
            return redirect('frntnd:home')
            
        else:
            print("Invalid OTP entered")
            return HttpResponse("Invalid OTP")

    return render(request, 'otpvalidate.html')


#  User account

def addaccount(request):
    return render(request)

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
        return redirect('frntnd:account')

    accounts = Useraccount.objects.filter(name = request.session['username'])

    return render(request, 'account.html', {'accounts': accounts})


def editaccnt(request, id):
    acc = Useraccount.objects.get(id=id)
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
        return redirect('frntnd:account')
    return render(request, 'editaccnt.html', {'acc': acc})


def deleteaccount(id):
    accound = Useraccount.objects.get(id=id)
    accound.delete()
    return redirect('frntnd:account')
  


    #  cart db ilkii evdna data varniii     
@login_required
def cart(request):
    prodt = Product.objects.filter(user= request.session['username'])
    return render(request, 'cart.html', {'prodt': prodt})  


def addcart(request, id):
    product = get_object_or_404(Product, id=id)
    cartitem = Cart.objects.get_or_create(prodt=product)
    return redirect('frntnd:cart',  {'product':product, 'cartitem':cartitem})
    

def cartremove(id):
    cartt = Cart.objects.get(id=id) 
    cartt.delete()
    return redirect('frntnd:cart')

@login_required
def checkout(request):
    return render(request, 'checkout.html')

@login_required
def contact(request):
    return render(request, 'contact.html')

@login_required
def whishlist(request):
    return render(request, 'whishlist.html')


# Helper function to generate OTP
def generate_otp():
    return str(random.randint(100000, 999999))


# def forget_password(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         associated_users = Register.objects.filter(email=email)
#         if associated_users.exists():
#             for user in associated_users:
#                 otp = generate_otp()
#                 request.session['reset_otp'] = otp
#                 request.session['email'] = email

#                 logger.debug(f"Generated OTP: {otp}")
#                 print(f"Generated OTP: {otp}")

#                 subject = "This is a password reset mail"
#                 message = f'Your OTP for resetting your password is {otp}.'
#                 send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
                
#                 return render(request, 'userapp1/newpassword.html')
#         return render(request, 'userapp1/forget_password.html', {'error': 'Email not found'})
#     return render(request, 'userapp1/forget_password.html')


def apps(request):
    if request.method=='POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:

            return HttpResponse("Heyy rght passwrd") 
        else:
            print("wrong")
        
    return render(request, 'apps.html')

