from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.
class Profile(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture=models.ImageField(upload_to='profile_images',default='default_profile_picture.png')
    profile_id=models.IntegerField
    bio=models.TextField()
    def __str__(self):
        return self.user.username
  
