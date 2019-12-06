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
        data = {'email': None}

        valid, response = validate_request_parameters(request, ['username', 'password'])
        if valid:
            authenticated, user_obj = authenticate_user(request, username=username, password=password)
            if authenticated:
                data['email'] = user_obj.email
                api_response['user'] = data
                return api_response
            else:
                raise APIError(message="Invalid credentials", status=401)
        else:
            raise APIError(message=response, status=400)


class SignupView(generics.CreateAPIView):
    # Return token in response

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        # TODO: 30/11/2019 Rajas add email validation here

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
