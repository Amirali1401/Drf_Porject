from rest_framework import  serializers

from django.contrib.auth.models import User

class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','email' ,'password']


    def validated_username(self ,obj):
        if obj  == 'admin':
            raise serializers.ValidationError('Your username must not be admin')

        return obj