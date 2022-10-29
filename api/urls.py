from datetime import datetime
from django.urls import path

from . import views

urlpatterns = [
    path('inventory/<str:id>/', views.inventory, name='inventory'),
    path('agent/<str:id>/', views.getAgentInfo, name='getAgentInfo'),
    path('getAll/',views.getAllAgents, name='getAllAgents'),
]