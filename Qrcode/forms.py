from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.views.generic.edit import FormView

from .models import *


class QrCodeForm(forms.ModelForm):

    class Meta:
        model = GenarateCode

        fields = '__all__'
