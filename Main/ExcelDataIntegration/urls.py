from django.urls import path
from . import views

urlpatterns = [
    path('import/', views.import_form, name='import_form'),
    
]