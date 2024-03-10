from django.urls import path
from . import views

urlpatterns = [
    path('generate-list/',views.generate_list, name='generate_list'),
    path('generated-list/',views.generated_list,name='generated_list')
]
