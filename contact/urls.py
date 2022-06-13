from  django.urls import path
from .views import contact_view

app_name = 'posts'

urlpatterns = [
    path('', contact_view, name='contact')
]
