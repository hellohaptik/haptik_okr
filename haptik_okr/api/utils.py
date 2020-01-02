import secrets
import string

from django.contrib.auth import authenticate
from api.models.okr_related import Sheet
from api.models.user_related import Team
from django.contrib.auth.models import User
from api.okr_encryption import decrypt_user_id


def validate_request_parameters(request, list_of_required_params):
    """
    This method checks if all the required parameters for the request is sent by the clients.

    :param request: instance of the request that is received from the client
    :param list_of_required_params: the list of parameters that are required in the request
    :return: returns a tuple containing a boolean, denoting the status of the validations and a string containing the
    error message. error string will be none if the validations are successful
    """
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
    """
    This method authenticates the user

    :param request: instance of the request that is received from the client
    :param username: string username of the user
    :param password: string password of the user
    :return: returns true if the user is authenticated, false otherwise and an instance of user class
    The instance of the user will be None if the username and password are not present in the DB
    """
    user_obj = authenticate(request, username=username, password=password)
    return user_obj is not None, user_obj


def generate_random_string_token(length):
    """
    This method returns random alpha-numeric values as token

    :param length: the length of the token required
    :return: alpha-numeric string
    """
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(length))


def check_user_permission(request, sheet_id):
    """
    This method returns if the user is the head of the team, whose sheet is being accessed

    :param request: request fired by the user
    :param sheet_id: id of the sheet being accessed by the user

    :return: true if the user is the head of the team, false other wise
    """
    valid, data = get_user_auth_token(request)
    user_name = decrypt_user_id(data)
    if valid:
        user = User.objects.get(username=user_name)
        sheet = Sheet.objects.get(pk=sheet_id)
        team = Team.objects.get(pk=sheet.team_id_id)
        return user.id == team.head_id
    else:
        return False


def get_user_auth_token(request):
    try:
        token = request.META['HTTP_AUTHORIZATION']
        if token:
            return True, token
        else:
            return False, "Authorization token missing"
    except KeyError as e:
        return False, "Unauthorized request"
