from django.contrib import messages
from django.shortcuts import render, redirect

def my_login_required(func):
    def wrapper(request, *args, **kwargs):
        messages.info(request,"Kindly Login Before Accesing")
        return redirect('login')
    return wrapper