from django.urls import path
from . import views

urlpatterns = [
path('', views.add_inventory, name='add_menu'),
]