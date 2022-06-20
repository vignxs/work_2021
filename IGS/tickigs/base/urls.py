from turtle import update
from django.urls import path
from . import views
urlpatterns = [
    path('customers/', views.ShowAll, name = 'ALL Customers'),
    path('techs/', views.Tech, name = 'Technology'),
    path('one/<int:pk>/', views.ShowOne, name = 'Customer'),
    path('create-customer/', views.Createcustomer, name = 'Create Customer'),
    path('update-customer/<int:pk>', views.Update, name='Update Customer'),
    path('delete-customer/<int:pk>', views.Delete, name='Delete Customer')
    
    ]
