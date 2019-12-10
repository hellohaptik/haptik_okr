import json

from django.contrib.auth import authenticate
from django.http import HttpResponse


def validate_request_parameters(request, list_of_required_params):
    '''
    This method checks if all the required parameters for the request is sent by the clients.

    :param request: instance of the request that is received from the client
    :param list_of_required_params: the list of parameters that are required in the request
    :return: returns a tuple containing a boolean, denoting the status of the validations and a string containing the
    error message. error string will be none if the validations are successful
    '''
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
    '''
    This method authenticates the user

    :param request: instance of the request that is received from the client
    :param username: string username of the user
    :param password: string password of the user
    :return: returns true if the user is authenticated, false otherwise and an instance of user class
    The instance of the user will be None if the username and password are not present in the DB
    '''
    user_obj = authenticate(request, username=username, password=password)
    return user_obj is not None, user_obj
