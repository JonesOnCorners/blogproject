from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import logging
from useraccounts.forms import CreateUserForm
from blog.decoraters import my_login_required




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

@login_required
def profile(request):
    context = {}
    return render(request, 'useraccounts/profile.html',context)
