from functools import wraps
from api.api_response import ApiResponse
from api.exceptions import APIError
from api.okr_encryption import decrypt_user_id
from django.contrib.auth.models import User
from api.utils import get_user_auth_token

from django.http import HttpResponse


def send_api_response(method):
    @wraps(method)
    def wrapper(request, *args, **kwargs):
        api_response = ApiResponse()
        try:
            api_response.success = True
            api_response.body = method(request, *args, **kwargs)
        except APIError as e:
            api_response.success = False
            api_response.error = e.message
            api_response.status_code = e.status
        return api_response.toHttpResponse()

    return wrapper


def authenticate_user(method):
    @wraps(method)
    def wrapper(request, *args, **kwargs):
        valid, data = get_user_auth_token(request)
        if valid:
            user_name = decrypt_user_id(data)
            user_obj = User.objects.get(username=user_name)
            if user_obj:
                return method(request, *args, **kwargs)
            else:
                return raise_error("Unauthorized user", 401).toHttpResponse()
        else:
            return raise_error(data, 401).toHttpResponse()

    return wrapper


def raise_error(message, status):
    api_response = ApiResponse()
    api_response.success = False
    api_response.error = message
    api_response.status_code = status
    return api_response
