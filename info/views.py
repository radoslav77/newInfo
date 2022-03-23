from functools import cached_property
from django.forms.widgets import CheckboxInput
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.contrib.auth.models import update_last_login
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse
from django.http import JsonResponse
import json


from .models import *
from .forms import *
# Create your views here.


def index(request):
    neme = 'Hello There!!!'
    form = DishForm()
    # print(DishForm())
    return render(request, 'info/index.html', {
        'name': neme,
        'form': form
    })


def input_dish(request):
    return render(request, 'info/recipeInput.html')


def input_subrecipe(request):
    return render(request, 'info/recipeInput.html')


def menu(request):
    return render(request, 'info/recipeInput.html')


def beveridge(request):
    return render(request, 'info/recipeInput.html')


def recipe(request):
    return render(request, 'info/recipeInput.html')


@csrf_protect
def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    elif request.method == 'POST':
        form = registrationForm(request.POST or None)
        #group_name = request.POST['groups']
        #groups = Group.objects.all()
        # print(groups)
        # print(group_name)
        name = []
        # for i in groups:

        #   print(i)
        if form.is_valid():
            user = form.save()

            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=user.username,
                                password=raw_password)
            #group = Group.objects.get(name=group_name)
            # user.groups.add(group)
            # login user
            login(request, user)
            return redirect('index')
    else:
        form = registrationForm()
    return render(request, 'info/register.html', {'form': form})


@csrf_protect
def login_user(request):
    if request.user.is_authenticated:

        return redirect('index')
        # if not logged in then log in
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user_last_login = User.objects.get(username=username).last_login

            # Check credential
            user = authenticate(username=username, password=password)

            if user:
                if not user_last_login:
                    update_last_login(None, user=user)
                    return render(request, 'info/change-password.html', {
                        'user': user
                    })

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return render(request, 'info/login.html', {'error': "Your account has been desaibled."})

            else:
                return render(request, 'info/login.html', {'error': 'Invalid username or password. Try Again.'})

        return render(request, 'info/login.html')


@csrf_protect
def change_password(request, user):

    # print(user)
    if request.method == 'POST':
        u = User.objects.get(username=user)
        new_password = request.POST['password1']
        re_password = request.POST['password2']
        if new_password != re_password:
            return render(request, 'info/change-password.html', {
                'msg': 'Your password DO NOT mutch! Please try again! '
            })
        else:
            u.set_password(new_password)
            u.save()
            return redirect('login_user')
    return render(request, 'info/change-password.html')


def logout_user(request):
    if request.user.is_authenticated:

        logout(request)
        return redirect('login_user')
    else:
        return redirect('login_user')
