from django.urls import path
from . import views

app_name = 'frntnd'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('singleproduct/', views.singleproduct, name='singleproduct'),
    path('account/', views.account, name='account'),
    path('contact/', views.contact, name='contact'),
    path('category/<catname>', views.category, name='category'), # catname is an argument 
    path('whishlist/', views.whishlist, name='whishlist'),
    
]