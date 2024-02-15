from django.shortcuts import render,redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import login,authenticate

# Create your views here.
def home_page(request):
    return render(request,'index.html',{})

def about_page(request):
    return render(request,'about.html',{})

def products_page(request):
    return render(request,'products.html',{})

def services_page(request):
    return render(request,'services.html',{})


