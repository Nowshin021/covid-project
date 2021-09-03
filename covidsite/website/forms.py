from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.forms import ModelForm
from website.models import *

class NgoSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text = "Required valid email address")
    is_ngo = forms.BooleanField(initial=True)
    #check = forms.BooleanField(required=True)
    class Meta:
        model = User
        fields = ('email', 'name' , 'password1' , 'password2', 'is_ngo')

    def __init__(self, *args, **kwargs):
        super(NgoSignupForm, self).__init__(*args, **kwargs)

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


class DeleteUser(forms.ModelForm):
    class Meta:
       model = User
       fields = ['email', 'name']

    def __init__(self, *args, **kwargs):
        super(DeleteUser, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        





class EditProfile(forms.ModelForm):
    class Meta:
        model = NgoProfileModel
        fields = '__all__'
        exclude = ['user']

        
    def __init__(self, *args, **kwargs):
        super(EditProfile, self).__init__(*args, **kwargs)

        self.fields['bio'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['hospital'].widget.attrs['class'] = 'form-control'


class RequestForm(forms.ModelForm):
    class Meta:
        model = RequestModel
        fields = ['name','email','phone','address']