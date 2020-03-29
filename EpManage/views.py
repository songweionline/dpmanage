from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'EpManage/login.html')


def logout(request):
    return render(request, 'EpManage/logout.html')