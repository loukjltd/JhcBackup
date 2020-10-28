from django.shortcuts import render
from AppTwo.models import User


def show_home_page(request):
    return render(request, 'AppTwo/home.html')


def show_users_list(request):
    user_list = {'user': User.objects.all()}
    return render(request, 'AppTwo/users.html', context=user_list)