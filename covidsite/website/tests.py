from django.test import TestCase
from django.test import SimpleTestCase
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from .models import NgoProfileModel
from .forms import EditProfile
from django.shortcuts import reverse
# Create your tests here.
User= get_user_model()
NGO = NgoProfileModel()
class UserTestcase(TestCase):
    

    def setUp(self):
        user_a = User(email='dummy_User@email.com',name='Dummy_User')
        user_a.is_staff= True
        user_a.is_superuser=True
        user_a.set_password('asdfASDF123')
        self.user_a = user_a
        user_a.save()
        
      
        

    def test_user_exist(self):
        user_count = User.objects.all().count()
        user = User.objects.all()
        self.assertEqual(user_count , 1)
        print("(1)User exist test method : Assert Equal the count of user just made by the test code... \n\n")
        
        
        
    def test_user_email(self):
        test_email = self.user_a.email
        self.assertEqual(self.user_a.email , test_email)
        print("(2)User Email test method Assert Equal user email just made by the test code... \n\n")
        

    def test_user_password(self):
        test_pass = self.user_a.password
        self.assertEqual(self.user_a.password, test_pass)
        print("(3)User Password test method : Assert Equal user password just made by the test code... \n\n")



class NGO_test_case(TestCase):
    
    def setUp(self):
        user_b = User(email='dummyNGO_User@email.com',name='Dummy_NGO')
        user_b.is_staff= False
        user_b.is_superuser=False
        user_b.is_ngo=True
        user_b.set_password('asdfASDF123')
        user_b.bio = 'this is a dummy bio'
        user_b.address = 'Banani'
        user_b.phone ='1234567'
        user_b.ngo_division = 'Dhaka'
        self.user_b = user_b
        user_b.save()
        

    def test_NGO_email(self):
        test_email = self.user_b.email
        self.assertEqual(self.user_b.email , test_email)
        print("(4)NGO Email test method Assert Equal user email just made by the test code... \n\n")
        

    def test_NGO_password(self):
        test_pass = self.user_b.password
        self.assertEqual(self.user_b.password, test_pass)
        print("(5)NGO Password test method : Assert Equal user password just made by the test code... \n\n")

    
    def test_NGO_bio(self):
        test_bio = self.user_b.bio
        self.assertEqual(self.user_b.bio, test_bio)
        print("(6)NGO Bio test method : Assert Equal NGO BIO just made by the test code... \n\n")

    def test_NGO_address(self):
        test_address = self.user_b.address
        self.assertEqual(self.user_b.address, test_address)
        print("(7)NGO Address test method : Assert Equal NGO Address just made by the test code... \n\n")


    def test_NGO_division(self):
        test_division = self.user_b.ngo_division
        self.assertEqual(self.user_b.ngo_division, test_division)
        print("(8)NGO Division test method : Assert Equal NGO Division just made by the test code... \n\n")

    def test_ngo_profile_form(self):
        
        form_data = {
            'bio' : 'this is a dummy bio',
            'address' :'Banani',
            'phone' : '1234567',
            'hostpital' : 'Medinova'
            #'ngo_division' : 'Dhaka'
        }
        form = EditProfile(data=form_data)
        self.assertEqual(form.is_valid(), True)
        
        print("(12)NGO edit profile  Form test method : Assert Equal NGO Profile form is valid or not... \n\n")
 



    


class URLTest(TestCase):
    def test_urls(self):
         response = self.client.get('/')
         self.assertEqual(response.status_code , 200)
         print("(9)URL test method : Assert Equal Homepage status code... \n\n")

    def test_url_homepage(self):
        response = self.client.get(reverse('HomeView'))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response, 'home.html')
        print("(10)Homepage  URL test method : Assert Equal Homepage status code... \n\n")

    def test_url_contactpage(self):
        response = self.client.get(reverse('ContactView'))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response, 'contact.html')
        print("(11)Contact Page  URL test method : Assert Equal Homepage status code... \n\n")
        
    
        




