"""
URL configuration for shoes project.

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('frntnd/', include('frntnd.urls')), 
    path('backnd/', include('backend.urls')),

]
