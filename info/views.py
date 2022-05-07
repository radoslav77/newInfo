from functools import cached_property

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


def detail(requets, title):
    detail_recipe = Dish_Recipe.objects.filter(title=title)
    sub_recipe = SharedRecipe.objects.filter(title=title)
    ing = []
    sub_title = []
    sub = []
    image = []
    portion_recipe = []
    portion_subrecipe = []

    for i in detail_recipe:
        picture_data = Dish.objects.filter(name=i.dish_title)
        portion_recipe.append(i.portions)
        for img in picture_data:
            image.append(img.image)
        if i.title == title:
            ing_lines = i.recipe.split(',')
            for line in ing_lines:
                ing.append(line)
            detail_subrecipe = SharedRecipe.objects.filter(dish_title=i.id)
            for r in detail_subrecipe:
                sub.append(r)
           # print(i.recipe)

    for sub_i in sub_recipe:
        sub_title.append(sub_i.title)
        portion_subrecipe.append(sub_i.portions)
        if sub_i.title == title:
            ing_lines = sub_i.recipe.split(',')
            for line in ing_lines:
                ing.append(line)
            detail_subrecipe = SharedRecipe.objects.filter(dish_title=sub_i.id)
            for r in detail_subrecipe:
                sub.append(r)
    # print(image)
    return render(requets, 'info/details.html', {
        'recipe': detail_recipe,
        'sub_title': sub_title,
        'ingrediant': ing,
        'subrecipe': sub,
        'image': image,
        'portions': portion_recipe,
        'portions_sub': portion_subrecipe

    })


def dishes(request):
    dish_data = Dish_Recipe.objects.all()
    starters = []
    mains = []
    desserts = []
    for d in dish_data:
        if d.type_dish == 'Starter':
            starters.append(d)
        elif d.type_dish == 'Main':
            mains.append(d)
        else:
            desserts.append(d)
    print(desserts)
    # return redirect('info:index')
    return render(request, 'info/dishes.html', {
        'starters': starters,
        'mains': mains,
        'desserts': desserts
    })


@csrf_protect
def input_dish(request):

    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        form1 = RecipeForm(request.POST, request.FILES)
        data = Dish.objects.all()
        title = request.POST['name']
        for d in data:
            if title == d.name:
                return render(request, 'info/input_dish.html', {
                    'form': form,
                    'error': 'There is a dish with that name!!! Please change the name!!!'
                })
        if form.is_valid and form1.is_valid:
            data = form.save(commit=False)
            data.save()
            data1 = form1.save(commit=False)
            data1.save()

        checked = request.POST.get('addrecipe', False)

        if checked == 'on':
            for_dish = request.POST['dish_title']
            type_dish = request.POST['type_dish']

            return render(request, 'info/input_subrecipe.html', {
                'title': for_dish,
                'type_dish': type_dish,
                'form': SharedRecipeForm()
            })

        return redirect('info:index')

    return render(request, 'info/input_dish.html', {
        'form': DishForm(),
        'form1': RecipeForm()
    })


@csrf_protect
def input_subrecipe(request):
    if request.method == 'POST':
        form = SharedRecipeForm(request.POST, request.FILES)
        if form.is_valid:
            data = form.save(commit=False)
            print(data)
            data.save()
            return redirect('info:index')
    form = SharedRecipeForm()
    return render(request, 'info/input_subrecipe.html', {
        'form': form
    })


def recipe_input(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid:
            data = form.save(commit=False)
            print(data)
            data.save()
            return redirect('info:index')
    form = RecipeForm()
    return render(request, 'info/recipeInput.html', {
        'form': form
    })


def allergent(request):
    if request.method == 'POST':
        form = AllergentForm(request.POST, request.FILES)
        if form.is_valid:
            data = form.save(commit=False)
            data.save()
            return redirect('info:allergent')
    return render(request, 'info/allergent-input.html', {
        'form': AllergentForm()
    })


def calory_input(request):
    if request.method == 'POST':
        form = CaloryForm(request.POST, request.FILES)
        if form.is_valid:
            data = form.save(commit=False)
            data.save()
            return redirect('info:calory_input')
    form = CaloryForm()
    return render(request, 'info/calory-input.html', {
        'form': form
    })


def wight_input(request):
    if request.method == 'POST':
        form = WightsForm(request.POST, request.FILES)
        if form.is_valid:
            data = form.save(commit=False)
            data.save()
            return redirect('info:wight_input')
    return render(request, 'info/wight-input.html', {
        'form': WightsForm()
    })


@csrf_protect
def menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid:
            data = form.save(commit=False)
            data.save()
        return redirect('info:index')
    form = MenuForm()
    return render(request, 'info/menu.html', {
        'form': form
    })


@csrf_protect
def beveridge(request):
    form = BeverageForm()
    return render(request, 'info/beveridge.html', {
        'form': form
    })

# Need to work on the commit of the form !!!!


@csrf_protect
def register(request):
    if request.user.is_authenticated:
        return redirect('info:index')

    elif request.method == 'POST':
        form = registrationForm(request.POST or None)
        # group_name = request.POST['groups']
        # groups = Group.objects.all()
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
            # group = Group.objects.get(name=group_name)
            # user.groups.add(group)
            # login user
            login(request, user)
            return redirect('info:index')
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
                    return redirect('info:index')
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
            return redirect('info:login_user')
    return render(request, 'info/change-password.html')


def logout_user(request):
    if request.user.is_authenticated:

        logout(request)
        return redirect('info:login_user')
    else:
        return redirect('info:login_user')


# API views
def calory_data(request):
    data = Calory.objects.all()
    calory_data = []

    for i in data:
        # calory per 1 gram
        amn = i.calory / 100

        calory_data.append({
            'title': i.item,
            'unit': i.unit,
            'amount': i.amout,
            'Kcal': amn,
        })
    # print(recipe_data)
    return HttpResponse(json.dumps(calory_data), content_type="application/json")


def wight_data(request):
    data = Wights.objects.all()
    wight_data = []
    for i in data:
        wight_data.append({
            'title': i.title,
            'amout': i.amout,
            'wight in g': str(i.wight) + ' ' + 'g',

        })
    # print(recipe_data)
    return HttpResponse(json.dumps(wight_data), content_type="application/json")


def recipe_data(request):
    recipe = Dish_Recipe.objects.all()
    subrecipe = SharedRecipe.objects.all()
    res = []
    sub_res = []

    for i in recipe:
        res.append({
            'title': i.title,
            'for Dish': i.dish_title,
            'outlet': i.outlet,
            'type': i.type_dish,
            'portions': i.portions,
            'recipe': i.recipe,
            'method': i.method,
            # 'date': i.date,
            'archived': i.archived,
            'shared': i.shared,
        })
    for j in subrecipe:

        sub_res.append({
            'title': j.title,
            'for Dish': j.dish_title.title,
            # 'outlet': i.outlet,
            'type': j.type_dish,
            'portions': j.portions,
            'recipe': j.recipe,
            'method': j.method,
            # 'date': j.date,
            'archived': j.archived,

        })
    result = [*res, *sub_res]
    return HttpResponse(json.dumps(result), content_type="application/json")


def allergen_data(request):
    data = Allergents.objects.all()
    allergen_data = []

    for i in data:
        allergen_data.append({
            'title': i.title,
            'type': i.allergent,
            'description': i.description,
            # 'data': i.date
        })
    return HttpResponse(json.dumps(allergen_data), content_type="application/json")
