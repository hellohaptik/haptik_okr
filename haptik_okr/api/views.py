import json

from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.decorators import method_decorator

from api.utils import validate_request_parameters, authenticate_user

# Create your views here.

from django.http import HttpResponse
from rest_framework import generics
from api.exceptions import APIError
from api.okr_decorators import send_api_response


class LoginView(generics.CreateAPIView):

    @method_decorator(send_api_response)
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        api_response = {'user': None, 'token': ''}
        data = {'username': None}

        valid, response = validate_request_parameters(request, ['username', 'password'])
        if valid:
            authenticated, user_obj = authenticate_user(request, username=username, password=password)
            if authenticated:
                data['username'] = user_obj.username
                api_response['user'] = data
                return api_response
            else:
                raise APIError(message="Invalid credentials", status=401)
        else:
            raise APIError(message=response, status=400)


class SignupView(generics.CreateAPIView):
    # Return token in response

    @send_api_response
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        api_response = {'user': None, 'token': ''}
        data = {'username': None}
        # TODO: 30/11/2019 Rajas add email validation here
        valid, response = validate_request_parameters(request, ['username', 'password'])
        if valid:
            # validate if the user already exists in the system
            user_exists, user = authenticate_user(request, username, password)
            if user_exists:
                raise APIError(message="User already exists, please sign up", status=400)
            try:
                user_obj = User.objects.create_user(username=username.lower(), password=password)
                if user_obj is not None:
                    user_obj.save()
                    data['username'] = user_obj.username
                    api_response['user'] = data
                    return api_response
            except:
                raise APIError(message="Failed to create user", status=500)
        else:
            raise APIError(message=response, status=400)
