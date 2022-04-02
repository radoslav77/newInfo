from typing import ChainMap
from django.urls import path
from . import views
from info import views

urlpatterns = [
    path('qr_code', views.index, name='code'),
]
