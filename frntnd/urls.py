from django.urls import path
from . import views
# from.views import simple_mail

app_name = 'frntnd'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('singleproduct/<int:id>', views.singleproduct, name='singleproduct'),


    path('account/', views.account, name='account'),
    path('deleteaccount/<int:id>', views.deleteaccount, name='deleteaccount'),
    path('editaccnt/<int:id>', views.editaccnt, name='editaccnt'),
  

    path('contact/', views.contact, name='contact'),
    path('category/<catname>/', views.category, name='category'), # catname is an argument 
    path('whishlist/', views.whishlist, name='whishlist'),
    path('cart/<int:id>/', views.cart, name='cart'),
    path('cartremove/<int:id>', views.cartremove, name='cartremove'),
    path('checkout/', views.checkout, name='checkout'),
    

    path('register/', views.register, name='register'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('logout/', views.logout, name='logout'),
    path('forgotpassword/', views.frgotpassword, name='forgotpassword'),
    path('newpassword/', views.newpassword, name='newpassword'),
    path('otpgenerate/', views.otpgenerate, name='otpgenerate'),
    path('otpvalidate/', views.otpvalidate, name='otpvalidate'),
    # path('simple_mail/', views.simple_mail, name='simple_mail')
    path('apps/', views.apps, name='apps'),
    
]
