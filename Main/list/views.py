from django.shortcuts import render
from ExcelDataIntegration.models  import IncompleteGeneration
from .models import CompletedGeneration
from django.contrib.auth.decorators import login_required


@login_required
def generate_list(request):
    list = IncompleteGeneration.objects.all()
    return render(request,'generate-list.html',{'list': list})

@login_required
def generated_list(request):
    list = CompletedGeneration.objects.all()
    return render(request,'generated-list.html',{'list': list})

