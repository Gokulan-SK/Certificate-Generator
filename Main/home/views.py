from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'index.html',{})

def login_page(request):
    return render(request,'login.html',{})

def about_page(request):
    return render(request,'about.html',{})

def products_page(request):
    return render(request,'products.html',{})

def services_page(request):
    return render(request,'services.html',{})


