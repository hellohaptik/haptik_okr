from datetime import datetime, timedelta

# Create your views here.
from api.constants import RESET_PASSWORD_TOKEN_EXPIRY_IN_MINS
from api.exceptions import APIError
from api.models.user_related import RenewPasswordToken
from api.okr_decorators import send_api_response
from api.utils import validate_request_parameters, authenticate_user, generate_random_string_token
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.decorators import method_decorator
from rest_framework import generics


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
                raise APIError(message="User already exists, please login", status=400)
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


class ForgotPasswordView(generics.CreateAPIView):

    @method_decorator(send_api_response)
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        valid, response = validate_request_parameters(request, ['username'])
        if valid:
            # validate if the user already exists in the system
            user = User.objects.get(username=username)
            if user:
                random_token = generate_random_string_token(10)
                token_expiry_time = (datetime.now() + timedelta(minutes=RESET_PASSWORD_TOKEN_EXPIRY_IN_MINS))
                current_token = RenewPasswordToken.objects.filter(user=user)
                if current_token.count() > 0:
                    current_token = current_token[0]
                    current_token.token = random_token
                    current_token.expiry = token_expiry_time
                else:
                    current_token = RenewPasswordToken(token=random_token, user=user, expiry=token_expiry_time)
                current_token.save()
                # Make a call to Mailer Service by sending the random_token as email
                return 'Reset Token Will be sent on following email %s' % user.username
            else:
                raise APIError(message="User does not exist", status=200)
        else:
            raise APIError(message=response, status=400)


class ResetForgottonPasswordView(generics.CreateAPIView):

    @method_decorator(send_api_response)
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        new_password = request.data.get("password", "")
        reset_token = request.data.get("reset_token", "")
        valid, response = validate_request_parameters(request, ['username', 'password', 'reset_token'])
        if valid:
            # validate if the user already exists in the system
            user = User.objects.get(username=username)
            if user:
                current_token = RenewPasswordToken.objects.filter(user=user)
                if current_token.count() > 0 and current_token[0].token == reset_token:
                    current_token = current_token[0]
                    if current_token.expiry > timezone.now():
                        user = current_token.user
                        user.set_password(new_password)
                        user.save()
                        current_token.delete()
                        return 'New password set successfully'
                    else:
                        raise APIError(message="Token is expired", status=200)
                else:
                    raise APIError(message="Incorrect Token sent", status=200)
            else:
                raise APIError(message="User does not exist", status=200)
        else:
            raise APIError(message=response, status=400)
