from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
<<<<<<< HEAD
    path('generate-list/',views.generate_list, name='generate_list'),
    path('certificate-template/', views.certificate_template, name='certificate_template'),
    
=======
>>>>>>> ad1d21cf3999f0bc55e34d96f4501ba65aae2baf
]
