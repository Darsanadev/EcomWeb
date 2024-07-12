from django.urls import path
from. import views

app_name = 'backend'

urlpatterns = [
    
    path('index/', views.index, name='index'),
    
    path('categorydata/', views.categorydata, name='categorydata'),
    path('categorydisplay/', views.categorydisplay, name='categorydisplay'),
    path('categoryedit/<int:id>', views.categoryedit, name='categoryedit'),
    path('categorydelete/<int:id>/', views.categorydelete, name='categorydelete'),
    path('cate_list/<int:id>/', views.cate_list, name='cate_list'),

    path('brand/', views.brand, name='brand'),
    path('branddisplay/', views.branddisplay, name='branddisplay'),
    path('branddelete/<int:id>/', views.branddelete, name='branddelete'),
    path('brandedit/<int:id>/', views.brandedit, name='brandedit'),
    path('brand_list/<int:id>/', views.brand_list, name='brand_list'),

    path('prodata/', views.prodata, name='prodata'),  
    path('prodisplay/', views.prodisplay, name='prodisplay'),       
    path('proedit/<int:id>', views.proedit, name='proedit'),  
    path('prodelete/<int:id>/', views.prodelete, name='prodelete'),
    path('pro_list/<int:id>/', views.pro_list, name='pro_list'),

    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('user/', views.user, name='user'),
    path('orders/', views.orders, name='orders'),
    path('coupon/', views.coupon, name='coupon'),
    path('coupondisplay/', views.coupondisplay, name='coupondisplay'),
    path('couponedit/<int:id>', views.couponedit, name='couponedit'),


]
