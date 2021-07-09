from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from website.models import *

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text = "Required valid email address")

    class Meta:
        model = User
        fields = ('email', 'name' , 'password1' , 'password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        

class LoginForm(forms.Form):
    email = forms.CharField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']


    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'