from django.shortcuts import render

# Create your views here.


def index(request):
    neme = 'Hello There!!!'

    return render(request, 'info/index.html', {
        'name': neme
    })
