import json

from django.contrib.auth import authenticate
from django.http import HttpResponse


def validate_request_parameters(request, list_of_required_params):
    response = {'success': True, 'message': None}
    valid = True
    error_string = ''
    for required_param in list_of_required_params:
        if not request.data.get(required_param, ""):
            error_string = error_string + required_param + " is missing \n"
            response['success'] = False
            valid = False
    response['message'] = error_string
    return valid, response


def authenticate_user(request, username, password):
    user_obj = authenticate(request, username=username, password=password)
    return user_obj is not None
