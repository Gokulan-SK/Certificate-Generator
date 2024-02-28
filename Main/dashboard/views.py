from django.shortcuts import render,redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views
from ExcelDataIntegration.models  import IncompleteGeneration
# Create your views here.

def dashboard(request):
    list = IncompleteGeneration.objects.all
    return render(request,'dashboard.html',{'list': list})


@login_required
def generate_list(request):
    return render(request, 'generate-list.html',{})

@login_required
def certificate_template(request):
    return render(request, 'certificate-template.html', {})


