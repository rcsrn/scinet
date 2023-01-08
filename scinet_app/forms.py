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

class NewResearcherForm(forms.ModelForm):
    class Meta:
        model = GeneralUser
        fields = ["general_user_id", "username", "first_name", "last_name", "email", 
                "password", "age",]
        labels = {'general_user_id':"General user id", 'username':"Username", 'first_name':"First Name",
                 'last_name':"Last Name", 'email':"E-mail", 
                'password':"Password", 'age':"Age"}

# class NewPublicationForm(forms.ModelForm):
#     class Meta:
#         model = Publication
#         fields = ["publication_id", "username", "first_name", "last_name", "email", 
#                 "password", "age",]
#         labels = {'general_user_id':"General user id", 'username':"Username", 'first_name':"First Name",
#                  'last_name':"Last Name", 'email':"E-mail", 
#                 'password':"Password", 'age':"Age"}

