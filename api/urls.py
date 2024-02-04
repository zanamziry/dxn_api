from datetime import datetime
from django.urls import path

from . import views

urlpatterns = [
    path('inventory/<str:id>/', views.inventory, name='Inventory'),
    path('service_centers/',views.getAllCenters, name='Get All Service Centers'),
    path('dollarvalue/',views.getDollarValue, name='Get USD/IQD Price'),
    path('testLogin/',views.TestLogin, name='test username and password'),
    path('',views.getProducts, name='Get All Products'),
]