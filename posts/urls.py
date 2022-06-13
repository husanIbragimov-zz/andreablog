from django.urls import path
from .views import home_view, single_view, about_view, fashion_view, travel_view

app_name = 'post'  # {% url 'app_name:urlname' %}

urlpatterns = [
    path('', home_view, name='home'),
    path('single/<slug:slug>/', single_view, name='single'),
    path('about/', about_view, name='about'),
    path('fashion/', fashion_view, name='fashion'),
    path('travel/', travel_view, name='travel'),
]
