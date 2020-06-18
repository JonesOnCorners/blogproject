from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from useraccounts.forms import CreateUserForm
from django.contrib import messages
import logging


# Create your views here.

def register(request):
    if request.method == 'POST':
        print("INSIDE REGISTER POST")
        form  = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account Created for {username}")
            return redirect('index')
        else:
            print("FORM ISSUE")
    else:
        form = CreateUserForm()
    context = {'form' : form}
    return render(request, 'useraccounts/register.html',context)
