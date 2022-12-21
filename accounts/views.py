from django.shortcuts import render
from django.contrib.auth.models import User

from .serializers import  UserRegisterSerializer



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny ,IsAuthenticated
# Create your views here.


class Register(APIView):
    permission_classes = [AllowAny ,]
    def post(self , request):
        ser_data = UserRegisterSerializer(data = request.data)

        if ser_data.is_valid():
            User.objects.create_user(
                username = ser_data.validated_data['username'],
                email = ser_data.validated_data['email'],
                password = ser_data.validated_data['password'],
            )

            return Response(ser_data.data , status=201)

        else:
            return Response(ser_data.errors , status = 404)