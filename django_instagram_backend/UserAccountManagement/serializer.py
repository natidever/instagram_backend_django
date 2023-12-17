from rest_framework import serializers 
from django.contrib.auth.models import User

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('username','password','email')
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
        return user 



