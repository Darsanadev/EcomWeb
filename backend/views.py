from django.shortcuts import render, get_object_or_404, redirect
from .models import  Category, Brand, Product

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
    return render(request, 'categorydata.html')  
        
def categorydisplay(request):
    cate = Category.objects.all()
    return render(request, 'categorydisplay.html', {'cate': cate})

def categoryedit(request):
    return render(request,'categorydisplay')

def categorydelete(request, id):
    cate = Category.objects.get(id=id)
    cate.delete()
    return redirect(categorydisplay)


# views of brands

def brand(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        description = request.POST.get('description')
        is_listed = request.POST.get('is_listed')
        brand = Brand(brand=brand, description=description, is_listed=is_listed)
        brand.save()  
    return render(request, 'brand.html')

def branddisplay(request):
    brand = Brand.objects.all()
    return render(request, 'branddisplay.html', {'brand': brand})

def branddelete(request, id):
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
        is_listed = request.POST.get('is_listed')  
        pro = Product(category=category, brand=brand, product=product, size=size, landing_price=landing_price, selling_price=selling_price, description=description, image=image, is_listed=is_listed)
        pro.save() 
    categories = Category.objects.all()
    brands = Brand.objects.all()
    return render(request, 'prodata.html', {'categories': categories, 'brands': brands})

def prodisplay(request):
    pro = Product.objects.all()
    cate = Category.objects.all()
    brand = Brand.objects.all()
    return render(request, 'prodisplay.html', {'pro': pro, 'cate': cate, 'brand': brand})

def proedit(request):
    return redirect('prodisplay')

def prodelete(request):
    return redirect('prodisplay')


def userdata(request):
    return render(request, 'userdata.html')

def data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES['image']
        dataa = Data(name=name, image=image)
        dataa.save()
    return render(request, 'data.html')

def display(request):
    dataa = Data.objects.all()
    return render(request, 'display.html', {'datta':dataa})

