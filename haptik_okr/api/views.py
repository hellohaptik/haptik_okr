import json

from django.contrib.auth.models import User
from django.shortcuts import render
from api.utils import validate_request_parameters, authenticate_user

# Create your views here.

from django.http import HttpResponse
from rest_framework import generics


class LoginView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")

        valid, response = validate_request_parameters(request, ['username', 'password'])
        if valid:
            authenticated = authenticate_user(request, username=username, password=password)
            if authenticated:
                response['message'] = "User logged in"
            else:
                response['success'] = False
                response['message'] = "No such user exists, please sign up"
            return HttpResponse(json.dumps(response), content_type='json')
        else:
            return HttpResponse(json.dumps(response), content_type='json')


class SignupView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")

        valid, response = validate_request_parameters(request, ['username', 'password', 'email'])
        if valid:
            # validate if the user already exists in the system
            if authenticate_user(request, username, password):
                response['success'] = False
                response['message'] = "User already exists, please sign up"
                return HttpResponse(json.dumps(response), content_type='json')

            try:
                user_obj = User.objects.create_user(username=username.lower(), email=email.lower(), password=password)
                if user_obj is not None:
                    user_obj.save()
                    response['message'] = "User created successfully"
            except:
                response['success'] = False
                response['message'] = "Failed to create user"
            return HttpResponse(json.dumps(response), content_type='json')
        else:
            return HttpResponse(json.dumps(response), content_type='json')
