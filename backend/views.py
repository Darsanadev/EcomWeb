from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import  Category, Brand, Product
from frntnd.models import Account

# Create your views here.           

def index(request):
    return render(request, 'index.html') 

# views of category 

def categorydata(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        description = request.POST.get('description')
        image = request.FILES['image']
        is_listed = request.POST.get('is_listed')  
        cate = Category(cname=cname, description=description, image=image, is_listed=is_listed)
        cate.save()
        if is_listed:
            message = f"Category '{cname}' is listed."
        else:
            message = f"Category '{cname}' is not listed."
        return HttpResponse(message)  # Simple response displaying the message
    return render(request, 'categorydata.html')  
        
def categorydisplay(request):
    cate = Category.objects.all()
    return render(request, 'categorydisplay.html', {'cate': cate})

def categoryedit(request, id):
   
    return render

def categorydelete(id):
    cate = Category.objects.get(id=id)
    cate.delete()
    return redirect('categorydisplay')

# views of brands

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

def branddisplay(request):
    brand = Brand.objects.all()
    return render(request, 'branddisplay.html', {'brand': brand})

def branddelete(id):
    brand = Brand.objects.get(id=id)
    brand.delete()
    return redirect(branddisplay)

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
    cate = Category.objects.all()
    brand = Brand.objects.all()
    return render(request, 'prodisplay.html', {'pro': pro, 'cate': cate, 'brand': brand})

# views of user 

def user(request):
    acc = Account.objects.all()
    return render(request, 'user.html', {'acc': acc})


def userdata(request):
    return render(request, 'userdata.html')


def proedit():
    return redirect('prodisplay')


def prodelete():
    return redirect('prodisplay')
