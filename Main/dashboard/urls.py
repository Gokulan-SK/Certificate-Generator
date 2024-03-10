from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('certificate-template/', views.certificate_template, name='certificate_template'),
    
]
