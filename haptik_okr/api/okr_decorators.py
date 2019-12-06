from functools import wraps
from api.api_response import ApiResponse
from api.exceptions import APIError

from django.http import HttpResponse


def send_api_response(method):
    def wrapper(request, *args, **kwargs):
        api_response = ApiResponse()
        try:
            api_response.success = True
            api_response.body = method(request, *args, **kwargs)
        except APIError as e:
            api_response.success = False
            api_response.body = e.message
        return api_response.toHttpResponse()

    return wrapper
