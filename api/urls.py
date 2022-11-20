from datetime import datetime
from django.urls import path

from . import views

urlpatterns = [
    path('inventory/<str:id>/', views.inventory, name='Inventory'),
    path('agent/<str:id>/', views.getAgentInfo, name='Get Agent Info'),
    path('agent/',views.getAllAgents, name='Get All Agents'),
    path('',views.getProducts, name='Get All Products'),
]