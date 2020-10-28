from django.shortcuts import render
from gourmetApp.models import Dishes, Material, User
from .forms import OrderForm, UserForm


def showPage(request):
    dict1 = {}
    Dishes.objects.get_or_create(dish_name='GBJD', price=15, rate=7.5)
    dict1['dish'] = Dishes.objects.all()[0]
    return render(request, 'gourmetApp/main.html', context=dict1)


def doAbc(request, year):
    return render(request, 'gourmetApp/dishes.html')


def showRec(request):
    return render(request, 'gourmetApp/dishes.html')


def gbjd(request):
    return render(request, 'gourmetApp/gbjd.html')


def order(request):
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        if form1.is_valid():
            dict1 = {'dishName': form1.cleaned_data['dishName'], 'number': form1.cleaned_data['number']}

        return render(request, 'gourmetApp/success.html', context=dict1)
    else:
        form = UserForm()
    dict2 = {'form': form}
    return render(request, 'gourmetApp/main.html', context=dict2)


def doRegister(request):
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        if form1.is_valid():
            dict1 = {'userName': form1.cleaned_data['userName'], 'password': form1.cleaned_data['password']}
            User.objects.get_or_create(username=dict1['userName'], password=dict1['password'])

        return render(request, 'gourmetApp/success1.html', context=dict1)
    else:
        form = UserForm()
    dict2 = {'form': form}
    return render(request, 'gourmetApp/register.html', context=dict2)


def doLogin(request):
    return render(request, 'gourmetApp/login.html')
