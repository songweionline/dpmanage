from django.contrib import admin
from django.urls import path
from . import views

app_name = 'EpManage'
urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]