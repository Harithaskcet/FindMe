from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('login/', login, name = "login"),
    path('signup/', signUp, name = "signUp"),
    path('logout/', logOut, name = "logOut"),
]
