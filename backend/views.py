from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import  Category, Brand, Product, Coupon
from frntnd.models import Useraccount
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from datetime import datetime, date

# Create your views here.       
    
def index(request):
    return render(request, 'index.html') 

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            return HttpResponse("Heyy... Welcom")
        else:
            messages.error(request, 'Invalid username or password')
            return HttpResponse("Invalid username or password")
    return render(request, 'adminlogin.html')


# views of category 

@login_required
def categorydata(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        description = request.POST.get('description')
        image = request.FILES['image']
        is_listed = request.POST.get('is_listed')  
        cate = Category(cname=cname, description=description, image=image, is_listed=is_listed)
        cate.save()
        return render(request, 'categorydata.html')
    return render(request, 'categorydata.html') 
 

def categorydisplay(request):
    cate = Category.objects.all()
    return render(request, 'categorydisplay.html', {'cate': cate})


def categoryedit(request, id): 
    categ = Category.objects.get(id=id)
    if request.method == 'POST':
        cname = request.POST.get('cname')
        description = request.POST.get('description')
        image = request.FILES['image']
        
        categ.cname = cname
        categ.description = description
        categ.image = image
        categ.save()
        return redirect('backend:categorydisplay')
    return render(request, 'categoryedit.html', {'categ': categ})

def categorydelete(id):
    catedelete = Category.objects.get(id=id)
    catedelete.delete()
    return redirect('backend:categorydisplay')

def cate_list(request, id):
    catelst = get_object_or_404(Brand, id=id)
    if request.method == 'GET':
        # catelst.is_listed = not catelst.is_listed  # Toggle the is_listed field

        if catelst.is_listed:
            catelst.is_listed=True
        else:
            catelst.is_listed=False

        catelst.save()
        return redirect('backend:categorydisplay')
    return redirect('backend:branddisplay')
       


# views of brands

def brand(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        description = request.POST.get('description')
        offer = request.POST.get('offer')
        is_listed = request.POST.get('is_listed')
        if Brand.objects.filter(brand=brand).exists():
            message = "Brand with this name alrdy exists."
            return render(request, 'brand.html', {"message": message})
        brand = Brand(brand=brand, description=description, offer=offer, is_listed=is_listed)
        brand.save()  
    return render(request, 'brand.html')


def branddisplay(request):
    brand = Brand.objects.all()
    return render(request, 'branddisplay.html', {'brand': brand})


def branddelete(id): 
    brand = Brand.objects.get(id=id)
    brand.delete() 
    return redirect('backend:branddisplay') 


def brandedit(request, id):
    bran = Brand.objects.get(id=id)
    if request.method == 'POST':
        brand = request.POST.get('brand')
        description = request.POST.get('description')
        offer = request.POST.get('offer')
        is_listed = request.POST.get('is_listed')
        
        bran.brand = brand
        bran.description = description
        bran.offer = offer
        bran.is_listed = is_listed
        bran.save()
        return redirect('backend:branddisplay')

    return render(request, 'brandedit.html', {'bran': bran})    

def brand_list(request, id):
    brandlst = get_object_or_404(Brand, id=id)
    if request.method=='GET':
        if brandlst.is_listed:
            brandlst.is_listed=False
        else:
            brandlst.is_listed=True

        brandlst.save()
        return redirect('backend:branddisplay')
    return redirect('backend:branddisplay')



# views of Products

def prodata(request):
    if request.method == 'POST':
        
        # Retrieve category and brand IDs from the form
        category_id = request.POST.get('category')
        brand_id = request.POST.get('brand')
        
        # Convert IDs to integers
        category_id = int(category_id)
        brand_id = int(brand_id)
        
        # Get Category and Brand instances
        category = Category.objects.get(id=category_id)
        brand = get_object_or_404(Brand, id=brand_id)
        
        product = request.POST.get('product')
        size = request.POST.get('size')                 
        landing_price = request.POST.get('landing_price')
        selling_price = request.POST.get('selling_price')
        offer = request.POST.get('offer')
        description = request.POST.get('description')   
        image = request.FILES['image'] 
        image1 = request.FILES['image1'] 
        image2 = request.FILES['image2'] 
        image3 = request.FILES['image3'] 
        is_listed = request.POST.get('is_listed')  
        pro = Product(category=category, brand=brand, product=product, size=size, landing_price=landing_price, selling_price=selling_price, offer=offer, description=description, image=image,image1=image1,image2=image2,image3=image3, is_listed=is_listed)
        pro.save()  
    categories = Category.objects.all()
    brands = Brand.objects.all()
    return render(request, 'prodata.html', {'categories': categories, 'brands': brands})
    

def prodisplay(request):
    pro = Product.objects.all()
    return render(request, 'prodisplay.html', {'pro': pro})
    

def proedit(request, id):
    prodt = Product.objects.get(id=id)
    if request.method=='POST':
        # category = request.POST.get('category')
        # brand = request.POST.get('brand')
        product = request.POST.get('product')
        size = request.POST.get('size')                 
        landing_price = request.POST.get('landing_price')
        selling_price = request.POST.get('selling_price')
        offer = request.POST.get('offer')
        description = request.POST.get('description')   
        # image = request.FILES['image']
        # image1 = request.FILES['image1']
        # image2 = request.FILES['image2']
        # image3 = request.FILES['image3']

        # prodt.category = category
        # prodt.brand = brand
        prodt.product = product
        prodt.size = size
        prodt.landing_price = landing_price
        prodt.selling_price = selling_price
        prodt.offer = offer
        prodt.description = description
        # prodt.image = image
        # prodt.image1 = image1
        # prodt.image2 = image2
        # prodt.image3 = image3
        prodt.save()
        return redirect('backend:prodisplay')
    return render(request, 'proedit.html', {'prodt': prodt})

def prodelete(id):
    prodel = Product.objects.get(id=id)
    prodel.delete()
    return redirect('backend:prodisplay')


def pro_list(request, id):
    prolst = get_object_or_404(Product, id=id)
    if request.method == 'GET':
        if prolst.is_listed:
            prolst.is_listed=False
        else:
            prolst.is_listed=True
        prolst.save()
        return redirect('backend:prodisplay')
    return redirect('backend:prodisplay')

# views of user 

def coupon(request):
    if request.method == 'POST':
        coupon = request.POST.get('coupon')
        amount = request.POST.get('discount')
        valid_from = request.POST.get('valid_from')
        valid_to = request.POST.get('valid_to')
        couponcode = Coupon(coupon=coupon, discount=amount, valid_from=valid_from, valid_to=valid_to)
        couponcode.save()
    return render(request, 'coupon.html')

now = date.today()
print("date of now ", now)

def coupondisplay(request):
    coupons = Coupon.objects.all()
    now = date.today()
    print("date of now is :", now)
    
    for coupon in coupons:
        if coupon.valid_from <= now <= coupon.valid_to:
            coupon.active = True
        else:
            coupon.active = False
        coupon.save()
    return render(request, 'coupondisplay.html', {'coupons': coupons})

def couponedit(request, id):
    coponcode = Coupon.objects.get(id=id)
    return render(request, 'couponedit.html', {'coponcode':coponcode})

def user(request):  
    acc = Useraccount.objects.all()
    return render(request, 'user.html', {'acc': acc})


def userblock(request):
    usrblck = Useraccount.objects.all()
    if usrblck.is_active():
        user.block
    else:
        user.unblock
    usrblck.save()
    return redirect('usrblck')


def orders(request):
    return render(request, 'Orders.html')

