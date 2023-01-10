from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class CustomTopicMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, topic):
        return "%s" % topic.name

class CustomInstitutionMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, institution):
        return "%s" % institution.name

class CustomJournalMCF(forms.ModelChoiceField):
    def label_from_instance(self, journal):
        return "%s" % journal.name

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
    username = forms.CharField(disabled=True)
    institutions = CustomInstitutionMMCF(queryset=Institution.objects.all(),
                    widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = GeneralUser
        fields = ["general_user_id", "username", "first_name", "last_name", "email", 
                "password", "age", "institutions"]
        labels = {'general_user_id':"General user id", 'username':"Username", 'first_name':"First Name",
                 'last_name':"Last Name", 'email':"E-mail", 
                'password':"Password", 'age':"Age", 'institutions':"Institutions"}

class EditProfileForm(forms.ModelForm):
    username = forms.CharField(disabled=True)
    institutions = CustomInstitutionMMCF(queryset=Institution.objects.all(),
                    widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = GeneralUser
        fields = ["username", "first_name", "last_name", "email", 
                 "age", "institutions"]
        labels = {'username':"Username", 'first_name':"First Name",
                 'last_name':"Last Name", 'email':"E-mail", 
                 'age':"Age", 'institutions':"Institutions"}


class NewPublicationForm(forms.ModelForm):
    journal_id = CustomJournalMCF(queryset=Journal.objects.all())
    publication_date = forms.DateField()
    topic = CustomTopicMMCF(queryset=Topic.objects.all(), 
                widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Publication
        fields = ["publication_id", "journal_id", "title", "publication_date", "content", 
                "doi", "topic",]
        labels = {'publication_id':"Publication id", 'journal_id':"Select journal", 
                'title':"Title", 'publication_date':"Publication Date", 'content':"Article", 
                'doi':"DOI", 'topic':"Topic"}

