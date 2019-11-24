import json

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework import generics


class LoginView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user_obj = authenticate(request, username=username, password=password)

        # if username or password is empty throw error
        if not username or not password:
            return HttpResponse(json.dumps({'status': False, 'error_code': 400, 'error_message': 'Username or password '
                                                                                                 'cannot be blank'}),
                                content_type='json')

        if user_obj is not None:
            return HttpResponse("User logged in")
        else:
            return HttpResponse("No such user exists, please sign up")


class SignupView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")

        if not username or not password or not email:
            return HttpResponse(json.dumps({'status': False, 'error_code': 400, 'error_message': 'Username or '
                                                                                                 'password or email '
                                                                                                 'cannot be blank'}),
                                content_type='json')

        # validate if the user already exists in the system
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return HttpResponse(
                json.dumps({'status': False, 'error_code': 400, 'error_message': 'User already exists, please signup'}),
                content_type='json')

        user_obj = User.objects.create_user(username=username.lower(), email=email.lower(), password=password)
        if user_obj is not None:
            user_obj.save()
            return HttpResponse("User created successfully")
        else:
            return HttpResponse("Failed to create user")
