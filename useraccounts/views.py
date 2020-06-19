from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import logging
from blog.decoraters import my_login_required
from useraccounts.forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from useraccounts.models import Profile




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
        p_form = ProfileUpdateForm()
    context = {'form' : form}
    return render(request, 'useraccounts/register.html',context)

@login_required
def profile(request):
    # user = Profile.objects.get(id=pk)
    # print(user)
    # context = {'user' : user}
    if request.method =='POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"Profile Updated Successfully !!!")
            return redirect('index')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        context = {'user_form' : user_form,
                   'profile_form' : profile_form}
    return render(request, 'useraccounts/userprofile.html', context)

