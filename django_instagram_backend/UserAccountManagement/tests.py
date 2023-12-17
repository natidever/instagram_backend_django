from django.test import TestCase

from rest_framework.test import APIClient,APITestCase
from rest_framework  import status
from django.contrib.auth.models import User

from .serializer import User_Serializer
from .models import Profile

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
      self.assertTrue(user.username,'Natnaelsisay')
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
         
   
        


      
    
