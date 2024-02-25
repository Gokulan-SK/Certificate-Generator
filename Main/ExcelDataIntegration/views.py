from django.shortcuts import render
<<<<<<< HEAD
from openpyxl import load_workbook
from .models import IncompleteGeneration

def import_from_excel(request):
    if request.method=='POST':
        excel_file=request.FILES['excel_file']
        wb=load_workbook(excel_file)
        ws=wb.active

        for row in ws.iter_rows(min_row=2, values_only=True):
            name, course, duration, email = row
            IncompleteGeneration.objects.create(name=name, course=course, duration=duration, email=email)

        return render(request, 'dashboard.html')

    return render(request, 'import_form.html')
=======

# Create your views here.
>>>>>>> ad1d21cf3999f0bc55e34d96f4501ba65aae2baf
