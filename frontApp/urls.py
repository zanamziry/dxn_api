from datetime import datetime
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]