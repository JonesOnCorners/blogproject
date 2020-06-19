from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from useraccounts.models import Profile


class CreateUserForm(UserCreationForm):
    email       = forms.EmailField()    

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


# class CreateUserForm(UserCreationForm):
#     email       = forms.EmailField()    
#     profile_pic = forms.ImageField()
#     class Meta:
#         model = User
#         fields = ['username','email','password1','password2']

#     def save(self, commit=True):
#         user = super(CreateUserForm, self).save(commit=False)
#         user.username = self.cleaned_data['username']        
#         user.email = self.cleaned_data['email']
#         user.password1 = self.cleaned_data['password1']
#         user.password2 = self.cleaned_data['password2']
    
#         # user has to be saved to add profile
#         user.save()        
#         user.profile_pic = self.cleaned_data.get('profile_pic')
#         user.profile.save()
    
#         if commit:
#             user.save()

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['first_name','middle_name','last_name','phone_number', 'address','profile_pic']
        #fields =['profile_pic']
        #fields = "__all__"
        #exclude = ['user']