from django.shortcuts import render
from .forms import *
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login

# Create your views here.


def login(request):
    if request.method == "GET":
        return render(request, 'EpManage/login.html')
    else:
        form = LoginForm(request.post)
        if form.is_valid():
            user_id = form.cleaned_data.get("user_id")
            password = form.cleaned_data.get("password")
            remember = int(request.POST.get("remember"))
    return render(request, 'EpManage/login.html')


def logout(request):
    return render(request, 'EpManage/logout.html')