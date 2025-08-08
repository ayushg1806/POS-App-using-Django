from django.urls import path
from products import views

urlpatterns = [
    path('', views.home, name='home'),  # loads the page with both forms
    path('add_product/', views.add_product, name='add_product'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('remove_product/<int:id>/', views.remove_product, name='remove_product'),
    path('remove_customer/<int:id>/', views.remove_customer, name='remove_customer'),
    path('invoice/', views.invoice_view, name='invoice'),
]