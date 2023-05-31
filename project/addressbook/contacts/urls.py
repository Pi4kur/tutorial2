from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]