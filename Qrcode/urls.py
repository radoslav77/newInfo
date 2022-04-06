from typing import ChainMap
from django.urls import path
from Qrcode import views

app_name = "Qrcode"

urlpatterns = [
    path('code/', views.code, name='code')
]
