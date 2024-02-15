from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Import Django's authentication views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('products/', views.products_page, name='products'),
    path('services/', views.services_page, name='services'),
]
