from django.urls import path
from .import views

urlpatterns=[
    path('',views.apiDOC,name='apidoc'),
    path('singup/',views.signup,name='signup'),
    path('login/',views.login_user,name='login'),
    path('userdata/',views.userdata,name='userdata'),
    path('upload-profile-picture/',views.upload_profile_picture,name='upload_profile_picture'),
    path('update-profile/',views.update_profile,name='updating_profile')
    
    
]