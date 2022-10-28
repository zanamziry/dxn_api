from datetime import datetime
from django.urls import path

from . import views

urlpatterns = [
    path('inventory/<str:id>/<str:date>/', views.inventory, name='inventory'),
    path('agent/<str:id>/', views.getAgentInfo, name='getAgentInfo'),
    path('add-agent/', views.addAgent, name='addAgent'),
]