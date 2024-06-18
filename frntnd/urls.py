from django.urls import path
from . import views
# from.views import simple_mail

app_name = 'frntnd'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('category/<catname>/', views.category, name='category'), # catname is an argument 
    path('singleproduct/<int:id>', views.singleproduct, name='singleproduct'),


    path('account/', views.account, name='account'),
    path('deleteaccount/<int:id>', views.deleteaccount, name='deleteaccount'),
    path('editaccnt/<int:id>', views.editaccnt, name='editaccnt'),
    

    path('register/', views.register, name='register'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('logout/', views.logout, name='logout'),
    path('forgotpass/', views.forgotpass, name='forgotpass'),
    path('newpassword/', views.newpassword, name='newpassword'),
    path('otpgenerate/', views.otpgenerate, name='otpgenerate'),
    path('otpvalidate/', views.otpvalidate, name='otpvalidate'),
  # path('simple_mail/', views.simple_mail, name='simple_mail')
    path('apps/', views.apps, name='apps'),

    
    path('contact/', views.contact, name='contact'),
    path('whishlist/', views.whishlist, name='whishlist'),
    path('cart/', views.cart, name='cart'),
    path('cartremove/<int:id>', views.cartremove, name='cartremove'),
    path('addcart/<int:id>', views.addcart, name='addcart'),
    path('checkout/', views.checkout, name='checkout'),

    
]
