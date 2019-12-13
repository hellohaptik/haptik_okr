import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from api.models.okr_related import Objective, Sheet
from api.utils import validate_request_parameters
from api.exceptions import APIError
from api.okr_decorators import send_api_response
from api.constants import INVALID_REQUEST
from django.core.exceptions import ObjectDoesNotExist


def populate_response_data(objective):
    api_response = {'objective': None}
    data = {
        'id': objective.id,
        'sheet_id': objective.quarter_sheet_id,
        'title': objective.title,
        'progress': objective.progress
    }
    api_response['objective'] = data
    return api_response


class ObjectiveView(APIView):

    @method_decorator(send_api_response)
    def post(self, request):
        # TODO: check if user can create the Objective based on the information in header
        request_body = json.loads(request.body)
        valid, response = validate_request_parameters(request, ['sheet_id', 'title'])
        if valid:
            try:
                sheet_id = int(request_body.get('sheet_id'))
                title = str(request_body.get('title'))
                sheet = Sheet.objects.get(pk=sheet_id)
                objective = Objective.objects.create(title=title, quarter_sheet=sheet, progress=0)
                return populate_response_data(objective)
            except (ValueError, ObjectDoesNotExist) as e:
                raise APIError(message=INVALID_REQUEST, status=400)
        else:
            raise APIError(message=response, status=400)


class ObjectiveDetailView(APIView):

    @method_decorator(send_api_response)
    def put(self, request, objective_id):
        # TODO: check if user can update the Objective based on the information in header
        request_body = json.loads(request.body)
        valid, response = validate_request_parameters(request, ['title'])
        if valid:
            try:
                # TODO explore serializers and try to optimize this code, create a object for every post, put request
                #  and try and serialize requests into that also for the responses
                objective_id = int(objective_id)
                objective_title = str(request_body.get('title'))
                objective = Objective.objects.get(pk=objective_id)
                objective.title = objective_title
                objective.save()
                return populate_response_data(objective)
            except (ValueError, Objective.DoesNotExist) as e:
                raise APIError(message=INVALID_REQUEST, status=400)
        else:
            raise APIError(message=response, status=400)