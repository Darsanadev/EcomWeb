from django.urls import path
from. import views

app_name = 'backend'

urlpatterns = [
    path('index/', views.index, name='index'),

    path('categorydata/', views.categorydata, name='categorydata'),
    path('categorydisplay/', views.categorydisplay, name='categorydisplay'),
    path('categoryedit/<int:id>', views.categoryedit, name='categoryedit'),
    path('categorydelete/<int:id>/', views.categorydelete, name='categorydelete'),

    path('prodata/', views.prodata, name='prodata'),
    path('prodisplay/', views.prodisplay, name='prodisplay'),
    path('proedit/', views.proedit, name='proedit'),
    path('prodelete/<int:id>/', views.prodelete, name='prodelete'),

    path('brand/', views.brand, name='brand'),
    path('branddisplay/', views.branddisplay, name='branddisplay'),
    path('branddelete/<int:id>/', views.branddelete, name='branddelete'),

    path('userdata/', views.userdata, name='userdata'),
   

]
