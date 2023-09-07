from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = "index.html"

class ProfileView(TemplateView):
    template_name = "profile.html"