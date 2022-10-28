from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    # ex: /polls/5/
    #path('inventory/<str:id>/<str:password>/<str:username>/', views.inventory, name='inventory'),
    path('inventory/<str:id>/<str:date>/', views.inventory, name='inventory'),
    path('agent/<str:id>/', views.getAgentInfo, name='getAgentInfo'),
    path('add-agent/', views.addAgent, name='addAgent'),

]