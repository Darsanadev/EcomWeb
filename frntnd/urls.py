from django.urls import path
from . import views

app_name = 'frntnd'

urlpatterns = [
    path('about/', views.about, name='about'),
    
]