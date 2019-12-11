import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from api.models.okr_related import Objective, Sheet
from api.utils import validate_request_parameters
from api.exceptions import APIError
from api.okr_decorators import send_api_response
import api.constants


class ObjectiveView(APIView):

    @method_decorator(send_api_response)
    def post(self, request):
        # TODO: check if user can create the Objective based on the information in header
        api_response = {'objective': None}

        request_body = json.loads(request.body.decode(encoding='UTF-8'))
        valid, response = validate_request_parameters(request, ['sheet_id', 'title'])
        if valid:
            try:
                sheet_id = int(request_body.get('sheet_id'))
                title = str(request_body.get('title'))

                sheet = Sheet.objects.get(pk=sheet_id)
                objective = Objective.objects.create(title=title, quarter_sheet=sheet, progress=0)
                data = {
                    'id': objective.id,
                    'sheet_id': sheet_id,
                    'title': objective.title,
                    'progress': objective.progress
                }
                api_response['objective'] = data
                return api_response
            except ValueError as e:
                raise APIError(message=api.constants.INVALID_REQUEST, status=400)
        else:
            raise APIError(message=response, status=400)
