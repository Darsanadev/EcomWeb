from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import  Category, Brand, Product
from frntnd.models import Useraccount
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

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
 
@login_required
def categorydisplay(request):
    cate = Category.objects.all()
    return render(request, 'categorydisplay.html', {'cate': cate})

@login_required
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
        return redirect('categorydelete')
    return render(request, 'categoryedit.html', {'categ': categ})

def categorydelete(id):
    catedelete = Category.objects.get(id=id)
    catedelete.delete()
    return redirect('categorydisplay')

def cate_list(request, id):
    catelst = get_object_or_404(Brand, id=id)
    if request.method == 'GET':
        # catelst.is_listed = not catelst.is_listed  # Toggle the is_listed field

        if catelst.is_listed:
            catelst.is_listed=True
        else:
            catelst.is_listed=False

        catelst.save()
        return redirect('catedisplay', id=id)
    return redirect('https://chatgpt.com/')
        

# views of brands

@login_required
def brand(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        description = request.POST.get('description')
        is_listed = request.POST.get('is_listed')
        if Brand.objects.filter(brand=brand).exists():
            message = "Brand with this name alrdy exists."
            return render(request, 'brand.html', {"message": message})
        brand = Brand(brand=brand, description=description, is_listed=is_listed)
        brand.save()  
    return render(request, 'brand.html')


@login_required
def branddisplay(request):
    brand = Brand.objects.all()
    return render(request, 'branddisplay.html', {'brand': brand})

 
def branddelete(id): 
    brand = Brand.objects.get(id=id)
    brand.delete() 
    return redirect('branddisplay') 


def brandedit(request, id):
    bran = Brand.objects.get(id=id)
    if request.method == 'GET':
        brand = request.POST.get('brand')
        description = request.POST.get('description')
        is_listed = request.POST.get('is_listed')
        
        bran.brand = brand
        bran.description = description
        bran.is_listed = is_listed
        bran.save()
        return redirect('branddisplay')
    return render(request, 'brandedit.html')    

def brand_list(request, id):
    brandlst = get_object_or_404(Brand, id=id)
    if request.method=='GET':
        if brandlst.is_listed:
            brandlst.is_listed=False
        else:
            brandlst.is_listed=True

        brandlst.save()
        return redirect('backend:brand_list')
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
        category = get_object_or_404(Category, id=category_id)
        brand = get_object_or_404(Brand, id=brand_id)
        
        product = request.POST.get('product')
        size = request.POST.get('size')                 
        landing_price = request.POST.get('landing_price')
        selling_price = request.POST.get('selling_price')
        description = request.POST.get('description')   
        image = request.FILES['image'] 
        image1 = request.FILES['image1'] 
        image2 = request.FILES['image2'] 
        image3 = request.FILES['image3'] 
        is_listed = request.POST.get('is_listed')  
        pro = Product(category=category, brand=brand, product=product, size=size, landing_price=landing_price, selling_price=selling_price, 
                      description=description, image=image,image1=image1,image2=image2,image3=image3, is_listed=is_listed)
        pro.save()  
    categories = Category.objects.all()
    brands = Brand.objects.all()
    return render(request, 'prodata.html', {'categories': categories, 'brands': brands})
    

def prodisplay(request):
    pro = Product.objects.all()
    return render(request, 'prodisplay.html', {'pro': pro})
    

def proedit(request, id):
    pro = Product.objects.get(id=id)
    if request.method=='POST':
        category = request.POST.get('category')
        brand = request.POST.get('brand')
        product = request.POST.get('product')
        size = request.POST.get('size')                 
        landing_price = request.POST.get('landing_price')
        selling_price = request.POST.get('selling_price')
        description = request.POST.get('description')   
        image = request.FILES['image']
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        image3 = request.FILES['image3']

        pro.category = category
        pro.brand = brand
        pro.product = product
        pro.size = size
        pro.landing_price = landing_price
        pro.selling_price = selling_price
        pro.description = description
        pro.image = image
        pro.image1 = image1
        pro.image2 = image2
        pro.image3 = image3
        pro.save()
        return redirect('prodisplay')
    return redirect('prodisplay')


def prodelete(id):
    prodel = Product.objects.get(id=id)
    prodel.delete()
    return redirect('prodisplay')


def pro_list(request, id):
    prolst = Product.objects.all()
    if prolst.is_listed:
        prolst.is_listed=True
    else:
        prolst.is_listed=False
    prolst.save()
    return redirect('pro_lst')


# views of user 

def user(request):  
    acc = Useraccount.objects.all()
    return render(request, 'user.html', {'acc': acc})


def userdata(request):
    return render(request, 'userdata.html')
