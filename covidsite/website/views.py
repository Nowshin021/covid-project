from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from .forms import *
from website.models import *
# Create your views here.
def HomeView(request):
    return render(request, 'home.html', {})


def NGOListView(request):
    return render(request, 'NGO.html', {})



def NGOProfileView(request):
    return render(request, 'NGOProfile.html', {})



def RequestTestView(request):
    return render(request, 'request-test.html', {})



def SignupView(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('LoginView')
    else :
        form = SignupForm()

    context = {
        'form' : form
    }

    return render(request, 'Signup.html', context)


def LoginView(request):
    message = None
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)
                #messages.success(request, 'Loged in successfully.')
                return redirect('HomeView')
                
            else:
                return redirect('LoginView')
                messages.error(request, 'Username or Password is incorrect.')
        else:
            return render(request, 'Login.html', {'form': form})
    form = LoginForm()
    context = {
        'form': form,
        
    }
    return render(request, 'Login.html', context)


def ContactView(request):
    return render(request, 'contact.html', {})



def LogoutView(request):
    logout(request)
    return redirect('LoginView')
    #return render(request, 'home.html', {})