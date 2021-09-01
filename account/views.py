from django.shortcuts import render

from django.urls import  reverse_lazy
from django.views.generic import  CreateView
from .forms import CustomCreation
class SignUp(CreateView):
    form_class=CustomCreation
    success_url=reverse_lazy('login')
    template_name='signup.html'
