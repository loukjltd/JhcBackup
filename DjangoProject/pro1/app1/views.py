from django.shortcuts import render
from django.urls import reverse, resolve
from app1.models import Dishes, Material


def showPage(request):
    # dict1 = {}
    # dict1['key1'] = 'Network18 Tom'
    # print(reverse('abcPage', args=[1000]))
    # print(resolve('/2000/'))
    # return render(request, 'app1\main.html', context=dict1)
    material = Material.objects.first()
    return render(request, 'app1\\main.html', {'material': material})


def doAbc(request, year):
    return render(request, 'app1\\1.html')


def showRec(request):
    return render(request, 'app1\\1.html')


def gbjd(request):
    return render(request, 'app1\\gbjd.html')


def mpdf(request):
    return render(request, 'app1\\mpdf.html')


def tcpg(request):
    return render(request, 'app1\\tcpg.html')
