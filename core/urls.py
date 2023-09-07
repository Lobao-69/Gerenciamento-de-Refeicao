from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("profile/", ProfileView.as_view(), name="profile"),
]