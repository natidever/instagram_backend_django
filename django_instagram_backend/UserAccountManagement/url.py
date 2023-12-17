from django.urls import path
from .import views

urlpatterns=[
    path('',views.apiDOC,name='apidoc'),
    path('singup/',views.signup,name='signup')
]