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
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from api.okr_encryption import encrypt_user_id

INVALID_EMAIL_MESSAGE = 'Please enter valid email id'

api_response = {}
data = {}


class LoginView(generics.CreateAPIView):

    @method_decorator(send_api_response)
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        valid, response = validate_request_parameters(request, ['username', 'password'])
        if valid:
            try:
                validate_email(username)
            except ValidationError as e:
                raise APIError(message=INVALID_EMAIL_MESSAGE, status=400)
            authenticated, user_obj = authenticate_user(request, username=username, password=password)
            if authenticated:
                data['username'] = user_obj.username
                api_response['user'] = data
                api_response['token'] = encrypt_user_id(user_obj.username)
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
        valid, response = validate_request_parameters(request, ['username', 'password'])
        if valid:
            try:
                validate_email(username)
                # validate if the user already exists in the system
                user_exists, user = authenticate_user(request, username, password)
                if user_exists:
                    raise APIError(message="User already exists, please login", status=400)

                user_obj = User.objects.create_user(username=username.lower(), password=password)
                if user_obj is not None:
                    user_obj.save()
                    data['username'] = user_obj.username
                    api_response['user'] = data
                    api_response['token'] = encrypt_user_id(user_obj.username)
                    return api_response
                else:
                    raise APIError(message="Failed to create user", status=500)
            except ValidationError as e:
                raise APIError(message=INVALID_EMAIL_MESSAGE, status=400)
        else:
            raise APIError(message=response, status=400)


class ForgotPasswordView(generics.CreateAPIView):

    @method_decorator(send_api_response)
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        valid, response = validate_request_parameters(request, ['username'])
        if valid:
            try:
                # validate if the user already exists in the system
                validate_email(username)
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
            except ValidationError as e:
                raise APIError(message=INVALID_EMAIL_MESSAGE, status=400)
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
            try:
                validate_email(username)
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
            except ValidationError as e:
                raise APIError(message=INVALID_EMAIL_MESSAGE, status=400)
        else:
            raise APIError(message=response, status=400)
