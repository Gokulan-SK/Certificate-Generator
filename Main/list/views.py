from django.shortcuts import render
from ExcelDataIntegration.models  import IncompleteGeneration
# Create your views here.
def generate_list(request):
    list = IncompleteGeneration.objects.all

    return render(request,'generate-list.html',{'list': list})