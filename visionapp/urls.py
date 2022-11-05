import include
from django.contrib import admin
from django.urls import path
from . import views
import accounts

urlpatterns = [
    path('home', views.home, name='name'),
    path('', accounts.views.login, name='login'),
    # path('change_password/', views.change_password, name='change_password'),
     
]
