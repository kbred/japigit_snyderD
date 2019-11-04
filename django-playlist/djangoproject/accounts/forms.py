from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    office = forms.CharField()
    officer = forms.CharField()
    organization = forms.CharField()
    organization_member = forms.CharField()
    subscriber = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'office', 'officer', 'organization', 'organization_member', 'subscriber']
