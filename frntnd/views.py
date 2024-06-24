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
from django.contrib.auth import authenticate


# Create your views here.  

def home(request):
    cate = Category.objects.all() 
    brand = Brand.objects.all() 
    pro = Product.objects.all() 
    register = Register.objects.all() 
    return render(request, 'home.html', {'cate': cate, 'brand': brand, 'pro': pro, 'register':register})


def product(request): 
    pro = Product.objects.all() 
    for produt in pro:
        produt_brand = produt.brand.offer
        if produt.brand.offer > produt.offer:
            produt.great_offer = produt_brand
        else:
            produt.great_offer = produt.offer
    return render(request, 'product.html', {'pro': pro})


# def product(request): 
#     print("hello") 
#     products = Product.objects.all() 
#     for product in products: 
#         product_brand = product.brand
#         product_offer = product.offer if product.offer is not None else 0
#         brand_offer = product_brand.offer if product_brand.offer is not None else 0
        
#         if brand_offer > product_offer:
#             product.great_offer = brand_offer
#         else:
#             product.great_offer = product_offer
#     return render(request, 'product.html', {'products': products})


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
                message=f' Hey Your reset password link  {link}  click the link to reset password. valid only for next 1 hour Njoy... ',
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
# LAPTOP-MCU76LIH 5556



def addcart(request, product_id):
    produt = None
    if request.method=='POST':
        print("POST request received")
        if request.user.is_authenticated:
            print(" valid User ")
            
            product = get_object_or_404(Product, id=product_id)
            quantity=int(request.POST.get('quantity'))
            print(f"Quantity: {quantity}, Price: {price}")
            # cart = Cart(user=user, quantity=quantity, prodt=produt)
            # cart.save()

            # check the product is alrdy in cart increase the quantity of product 

            cart_item, created = Cart.objects.get_or_create(
                prodt=product, user=request.user, defaults={'quantity': quantity, 'price': product.price, 'total': product.price * quantity})
   
            if created:
                cart_item.quantity += quantity 
                return redirect('frntnd:cart')
            else:
                cart_item.quantity = quantity 
                cart_item.total = cart_item.quantity * cart_item.price
            cart_item.save()
            return HttpResponse("Product added to cart.")

        else:
            return redirect('frntnd:userlogin')
    else:
        produt = Product.objects.filter(id=product_id)
    return render(request, 'cart.html', {'produt': produt})



# def addcart(request, product_id):
#     if request.method == 'POST':
#         quantity = request.POST.get('quantity')
#         price = request.POST.get('price')
#         total = request.POST.get('total')
#         cartt = Cart(quantity=quantity, price=price, total=total)
#         cartt.save()
#         produt = Product.objects.filter(id=product_id)
#         produt.save()
#     return render(request, 'cart.html')




def cart(request):
    carts=Cart.objects.all()
    return render(request, 'cart.html', {'carts': carts})


# def addcart(request, product_id):
#     produt=None
#     if request.method=='POST':

#         if request.user.is_authenticated:
                
#             user = request.user 
#             produt = Product.objects.filter(id=product_id)
         
#             quantity = request.POST.get('quantity') # Default to 1 if not provided
            
#             price = request.POST.get('price')
#             cart_item, created = Cart.objects.get_or_create(product=product, user=user)
        
#             cart_item = Cart.objects.create(
#                prodt= produt, price=price)
#             cart_item.save()


#             # Check if the product is already in the cart
#             cart_item = Cart.objects.filter(produt=produt, user=request.user).first()
                
#             if cart_item:
#                 cart_item.quantity += 1
#                 cart_item.save()
#             else:
#                 cart_item = Cart(produt=produt, user=request.user, quantity=1)  
#                 cart_item.save() 

#         # cart_item, created = Cart.objects.get_or_create(product=product, user=user)
        
#         # if not created:
#         #     # If the cart item already exists, update the quantity
#         #     cart_item.quantity += quantity
#         # else:
#         #     # If it's a new cart item, set the quantity and price
#         #     cart_item.quantity = quantity
#         #     cart_item.price = price
#         #     cart_item.save()

#         return redirect('frntnd:cart')
    
       
#     cart_item = Product.objects.filter(id=product_id)
#     # car = Cart( prodt=produt)
#     # car.save()
#     return render(request, 'cart.html',  {'cart_item':cart_item})


# def addcart(request, product_id):
#     produt=None
#     if request.method=='POST':

        # user=request.user
        # quantity = int(request.POST.get('quantity', 1)) # Default to 1 if not provided
        # price = request.POST.get('price')
        # cart = Cart(quantity=quantity, price=price)
        # cart.save()
        # price = float(request.POST.get('price', product.price))  # Use product price if not provided
        
        # # Check if the user is authenticated
        # if request.user.is_authenticated:
        #     # Check if the product is already in the cart for the user
        #     cart_item, created = Cart.objects.get_or_create(
        #         user=request.user,
        #         prodt=product,
        #         defaults={'quantity': quantity, 'price': price, 'total': price * quantity}
        #     )

#         if request.user.is_authenticated: 
#             print("valid user") 
#             produt = get_object_or_404(Product, id=product_id) 
#             cart = Cart(produt=produt) 
#             cart.save()
            
#             # Check if the product is already in the cart
#             cart_item = Cart.objects.filter(produt=produt, user=request.user).first()
            
#             if cart_item:
#                 cart_item.quantity += 1
#                 cart_item.save()
#             else:
#                 cart_item = Cart(produt=produt, user=request.user, quantity=1)  
#                 cart_item.save()

#             # if the product is alrdy in cart increase the quantity of product 
#             return redirect('frntnd:cart', product_id=product_id)  
             
#         else:
#             return redirect('frntnd:userlogin')   
#     return render(request, 'cart.html',  {'produt':produt})
    

def quantity(request):

    if request.method=="POST":
        total = price*quantity
    return render(request, 'cart.html')

    
# def cart(request):
#     if request.user.is_authenticated:
#         produt = Cart.objects.filter(user= request.user) 

#     else:
#         # return HttpResponse("Nothng is heree")
#         return redirect('frntnd:userlogin')
#     return redirect('frntnd:cart', {'produt': produt}) 



def cartremove(id):
    # cartt = Cart.objects.get(id=id) 
    cartt = get_object_or_404(Cart, id=id)
    cartt.delete()
    return redirect('frntnd:cart')


def checkout(request):
   
    return render(request, 'checkout.html')


def contact(request):
    return render(request, 'contact.html')


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

