from django.shortcuts import render,redirect
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from .forms import *
from website.models import *
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

# Create your views here.

def HomeView(request):
    return render(request, 'home.html', {})



				
                
		

class NGOListView(ListView):
    model = NgoProfileModel    
    template_name = 'NGO.html'
    context_object_name = 'NGO_list'
    #return render(request, , {})				
					



def NGODetailView(request, pk):   
    context = {} 
    NGO = get_object_or_404(User, pk=pk)
    #NGO = request.user.ngoprofilemodel
    context['NGO'] = NGO
    #context['user'] = user
    return render(request, 'NGOProfile.html', context)


     
   
@login_required(login_url='LoginView')
def NGOProfileView(request):
    context = {}
    NGO = request.user.ngoprofilemodel
    context['NGO'] = NGO
    return render(request, 'Profile.html', context)



def RequestTestView(request):
    return render(request, 'request-test.html', {})



def SignupView(request):
    if request.method =='POST':
        print("Post called")
        form = NgoSignupForm(request.POST)
        if form.is_valid():
            
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            NgoProfileModel.objects.create(user=user)
            return redirect('LoginView')
        else :
            print("Not created")
            return render(request, 'Signup.html', {"form": form})
            
        
    else :
        form = NgoSignupForm()

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

            if user and user.is_ngo:
                login(request, user)
                #messages.success(request, 'Loged in successfully.')
                return redirect('NGOProfileView')
                
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


def EditProfileView(request):
    applicant = request.user.ngoprofilemodel
    form = EditProfile(instance=applicant)
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=applicant)
        if form.is_valid():
            form.save()
            return redirect('NGOProfileView')
        else:
            return redirect('edit_profile.html')   
    context = {
      
        'form': form,
    }
    return render(request, 'edit_profile.html', context)

def DeleteProfileView(request):    
    if request.method == 'POST':
        form = DeleteUser(request.POST, instance=request.user)
        if form.is_valid():
            form.instance.delete()
            return redirect('HomeView')
    form = DeleteUser(instance=request.user)
    args = {}
    args['form'] = form
    return render(request, 'delete_profile.html', args) 