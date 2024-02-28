from django.urls import path
from . import views

urlpatterns = [

    path('import/', views.import_form, name='import_form'),

    path('import/', views.import_from_excel, name='import_form'),

    
]