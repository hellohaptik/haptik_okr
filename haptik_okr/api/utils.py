import json

from django.contrib.auth import authenticate
from django.http import HttpResponse


def validate_request_parameters(request, list_of_required_params):
    valid = True
    missing_params = []
    for required_param in list_of_required_params:
        if not request.data.get(required_param, ""):
            missing_params.append(required_param + " is missing")
    error_string = ", ".join(missing_params)
    if len(error_string) > 0:
        valid = False
    return valid, error_string


def authenticate_user(request, username, password):
    user_obj = authenticate(request, username=username, password=password)
    return user_obj is not None, user_obj
