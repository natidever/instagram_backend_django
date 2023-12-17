from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import User_Serializer
from django.http import JsonResponse

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

    

