from django.shortcuts import render
from rest_framework.decorators import api_view,parser_classes,permission_classes,authentication_classes
from rest_framework.response import Response
from .serializer import User_Serializer,Profile_Serializer
from django.http import JsonResponse
from django.contrib.auth import login,authenticate
from rest_framework import status
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.parsers import MultiPartParser, FormParser

@api_view(['GET'])
def apiDOC(request):
    route = [
        {
            "EndPoint":"/api/",
            "body":" ",
            "Description":"note fetched from these end point"

        } 
    ]
    return Response(route)
    
 
   
# Create your views here.
@api_view(['POST'])
def signup(request):
    serializer = User_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        return JsonResponse(serializer.data,status=201)
    return JsonResponse(serializer.errors ,status=400)

@api_view(['POST'])
def login_user(request):
 
    username = request.data.get('username')
    password = request.data.get('password')
    user =authenticate(username=username,password=password)
    if user is not None:
            login(request,user)
            return Response({'status':'200'})
    else:
         return Response({'error':'Invalid password or username'},status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def userdata(request):
    #send profile model
    #  if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        profile=Profile.objects.get(user=user)
        serialized_profile = Profile_Serializer(profile)

        return Response( serialized_profile.data,  status=200)
    #  else:
    #       return Response(status=400)


@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser])
def upload_profile_picture(request):
     if 'profile_picture' not in request.FILES:
          return Response({'error':"file is not provided"},status=status.HTTP_400_BAD_REQUEST)
     file=request.FILES['profile_picture'] 
     user=request.user
     try:
          profile = Profile.objects.get(user = user)
     except Profile.DoesNotExist:
          return Response({'error':'profile is not found'},status=status.HTTP_404_NOT_FOUND)
     
          
     profile.profile_picture=file
     profile.save()
     return Response({'message':'profile picture uploded'},status=status.HTTP_200_OK)

@api_view(['POST','PUT'])
def update_profile(request):
  username = request.data.get('username')
  bio =request.data.get('bio')
  if username is not None:
      if User.objects.filter(username =username).exists():
          return  Response({'error':'username is already taken'},status=status.HTTP_409_CONFLICT)
      request.user.username = username

      request.user.save()
  try:
     profile = Profile.objects.get(user=request.user)
  except Profile.DoesNotExist:
     return Response({'error ':'Profile is not found '},status=status.HTTP_404_NOT_FOUND)    
  if bio is not None:
     profile.bio=bio
     profile.save()
  if bio is None :
    pass  
     
#   if username and bio is None:
#       return Response({'message':'no change occured'},status=status.HTTP_200_OK)
  
  return Response({'message ':'Profile updated'},status=status.HTTP_200_OK)      

     