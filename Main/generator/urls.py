from django.urls import path
from . import views

urlpatterns = [
    path('certificate/<int:id>/',views.edit,name='certificate'),
]
