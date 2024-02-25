from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('generate-list/',views.generate_list, name='generate_list'),
    path('certificate-template/', views.certificate_template, name='certificate_template'),
    
]
