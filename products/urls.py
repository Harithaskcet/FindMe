from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('create/', create, name = "create"),
    path('<int:product_id>', detail, name = "detail"),
    path('<int:product_id>/addVote', addVote, name="addVote"),
]
