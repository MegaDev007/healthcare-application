import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver


# Create your views here.

# function to return views for the urls


# def hospital_home(request):
#     return render(request, 'index-2.html')

# Create your views here.
