from typing import ChainMap
from django.urls import path
from Qrcode import views

app_name = "Qrcode"

urlpatterns = [
    path('code/', views.index1, name='index1'),
    path('codes', views.code, name='code')
]
