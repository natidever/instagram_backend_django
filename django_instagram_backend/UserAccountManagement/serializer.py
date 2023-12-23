from rest_framework import serializers 
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.response import Response
from django.contrib.auth import authenticate,login


class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['username','password','email']
        #To use the password only creating and updating the instance
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        username=validated_data.get('username')
        email=validated_data.get('email')
        password = validated_data.pop('password')
        if len(password)<=8:
            raise serializers.ValidationError("Password length must be more than 8")
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            raise serializers.ValidationError('username or email is taken')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        try:
         new_Profile=Profile(user=user)
         new_Profile.save()
        except Exception as e:
         print(f"Error creating profile: {e}")
        return user
class Profile_Serializer(serializers.ModelSerializer):
         user = User_Serializer(read_only=True)
         class Meta:

             model=Profile


             
             fields=['id','user','profile_picture','bio']

 
    


