from django.shortcuts import render,redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

# Create your views here.

@login_required
def dashboard(request):
    return render(request,'dashboard.html',{})

@login_required
def generate_list(request):
    return render(request, 'generate-list.html',{})

@login_required
def certificate_template(request):
    return render(request, 'certificate-template.html', {})


