from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as log_view
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.HomeView, name = "HomeView"),
    path('NGO/', views.NGOListView.as_view(), name = "NGOListView"),
    path('NGO/<int:pk>', views.NGODetailView, name = "NGODetailView"),
   # path('NGO-profile', views.NGOProfileView, name = "NGOProfileView"),
    path('Request-Test', views.RequestTestView, name = "RequestTestView"),
    path('Signup', views.SignupView, name = "SignupView"),
    path('Login', views.LoginView, name = "LoginView"),
    path('Log-Out', views.LogoutView, name = "LogoutView"),
    path('Contact', views.ContactView, name = "ContactView")
    
    
]
