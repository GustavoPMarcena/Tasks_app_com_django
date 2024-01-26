from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.loginview, name='loginpage'),
    path('registrar/', views.register, name='registerpage') 
]