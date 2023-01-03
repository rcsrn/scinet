from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# class NewResearcherForm(UserCreationForm):
#     first_name = forms.CharField(max_length=255, required=True)
#     last_name = forms.CharField(max_length=255, required=True)
#     email = forms.EmailField(required=True)
#     age = forms.IntegerField(required=True)

#     class Meta:
#         model = GeneralUser
#         fields = ("username", "first_name", "last_name", "email", 
#                 "password1", "password2", "age")
    
#     def save(self, commit=True):

