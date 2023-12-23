from django.test import TestCase
from rest_framework  import status
from django.contrib.auth.models import User
from .serializer import User_Serializer
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Profile
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate,APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.contrib.auth.models import User

from .views import upload_profile_picture,userdata,update_profile
class User_Serializer_Test(TestCase):
   def setUp(self):
      client = APIClient()
   def test_user_serializer(self):
      #we serialize the data and store it in database then we take out the assert it 
      user_data ={'username':'NatnaelSisay','password':'these9023','email':'natidev404@gmail.com'}
      serializer=User_Serializer(data=user_data)
      print(serializer.is_valid())
      print(serializer.errors)
    
      self.assertTrue(serializer.is_valid())
    
      user=serializer.save()
      new_profile=Profile(user=user)
      self.assertTrue(user.username,'Natnaelsisay')
      self.assertTrue(new_profile.user.username,'Natnaelsisay')
      username =new_profile.user.username 
      print('newProfile:'+username)
      self.assertTrue(user.email,'natidev404@gmail.com')


    #we test signup is the signup view accept the datafrom user using POST
    #as json the create an object?
class Signup_Test(APITestCase):
   
   def setUp(self):
      client=APIClient()
   def test_signup(self):
      user_data ={'username':'NatnaelSisay','password':'these9023','email':'natidev404@gmail.com'}
      response=self.client.post('/singup/',user_data,format='json' )
      self.assertEqual(response.status_code,status.HTTP_201_CREATED)
      self.assertEqual(User.objects.count(),1)
      self.assertEqual(User.objects.get().username,"NatnaelSisay")

class Login_Test(APITestCase):
   def setUp(self):
      #Create the user 
      self.credentials={
         'username':'NatnaelSisay',
         'password':'these9023'
      }
      self.new_user =User.objects.create_user(**self.credentials)
     
      
      
   def test_login_success(self):
      #it must validated
      response=self.client.post('/login/',self.credentials,follow=True)
    

      self.assertEqual(response.status_code,200)
class sending_user_data(APITestCase):
   #Client send API resquest at userdata endpoint and get response is 200
  def setUp(self):
     self.factory = APIRequestFactory()
     self.credentials={
         'username':'NatnaelSisay',
         'password':'these9023'
      }
     self.new_user =User.objects.create_user(**self.credentials)
     self.new_profile=Profile.objects.create(user=self.new_user)
     


  def test_user_data_is_sent(self):
     self.client.login(username='NatnaelSisay', password='these9023')
     request = self.factory.get('/userdata/')
     force_authenticate(request, user=self.new_user)
     response = userdata(request)

     self.assertEqual(response.status_code,200)
    



class Uploading_Profile_Picture(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.credentials = {
            'username': 'NatnaelSisay',
            'password': 'these9023'
        }
        self.new_user = User.objects.create_user(**self.credentials)
        self.new_profile = Profile.objects.create(user=self.new_user)

    def test_uploading_profile_picture(self):
        url = reverse('upload_profile_picture')
        image = SimpleUploadedFile('profilepic.png', b'file_content', content_type='img/png')
        request = self.factory.post(url, {'file': image}, format='multipart')
        force_authenticate(request, user=self.new_user)
        response = upload_profile_picture(request)
        self.new_profile.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.new_profile.profile_picture)
        self.assertEquals(response.status_code,200)


class updating_profile_(APITestCase):
   def setUp(self):
    self.factory = APIRequestFactory()
    self.credentials = {
            'username': 'NatnaelSisay',
            'password': 'these9023'
        }
    self.new_user = User.objects.create_user(**self.credentials)
    self.new_profile = Profile.objects.create(user=self.new_user)
    
   def test_updateing_profile(self):
      username = 'username'
      bio='bio'
      url=reverse('updating_profile')
      request=self.factory.post(url,{'username':username,'bio':bio})
      force_authenticate(request,user=self.new_user)
      response=update_profile(request)
      self.assertEqual(response.status_code,200)
      self.new_profile.refresh_from_db()
      self.new_user.refresh_from_db()
      self.assertEqual(bio,self.new_profile.bio)
      self.assertEqual(username,self.new_user.username)
      
      
       
    


      


      


         
   
        


      
    
