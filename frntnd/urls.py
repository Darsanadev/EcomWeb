from django.urls import path
from . import views
from.views import simple_mail

app_name = 'frntnd'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('checkout/', views.checkout, name='checkout'),
    path('singleproduct/<int:id>', views.singleproduct, name='singleproduct'),
    path('account/', views.account, name='account'),
    path('deleteaccount/<int:id>', views.deleteaccount, name='deleteaccount'),
    
    path('contact/', views.contact, name='contact'),
    path('category/<catname>/', views.category, name='category'), # catname is an argument 
    path('whishlist/', views.whishlist, name='whishlist'),
    path('cart/', views.cart, name='cart'),
    path('cart/', views.cart, name='cart'),
    path('removecart/<int:id>', views.removecart, name='removecart'),
    
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('otpgenerate/', views.otpgenerate, name='otpgenerate'),
    path('otpvalidate/', views.otpvalidate, name='otpvalidate'),
    path('simple_mail/', views.simple_mail, name='simple_mail')
    
]
