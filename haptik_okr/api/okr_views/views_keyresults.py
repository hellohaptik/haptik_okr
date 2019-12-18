from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework.views import APIView

from api.okr_decorators import send_api_response
import json

from api.utils import validate_request_parameters
from api.models.okr_related import Objective, KeyResults
from api.exceptions import APIError
from api.constants import INVALID_REQUEST


# TODO: check if we can write a util method to populate data given a dict of keys and corresponding objects
def populate_keyresults_data(keyresult):
    api_response = {}
    data = {
        'id': keyresult.id,
        'title': keyresult.title,
        'progress': keyresult.progress,
        'is_discarded': keyresult.is_discarded,
        'objective_id': keyresult.objective_id
    }
    api_response['keyresult'] = data
    return api_response


class KeyResultsView(generics.CreateAPIView):

    @method_decorator(send_api_response)
    def post(self, request, *args, **kwargs):
        # TODO: check if user can create the task based on the information in header
        request_body = json.loads(request.body)
        valid, response = validate_request_parameters(request, ['objective_id', 'title'])
        if valid:
            try:
                objective_id = int(request_body.get('objective_id'))
                title = str(request_body.get('title'))
                objective = Objective.objects.get(pk=objective_id)
                keyresult = KeyResults.objects.create(title=title, objective=objective, progress=0, is_discarded=False)
                keyresult.save()
                return populate_keyresults_data(keyresult)
            except (ValueError, KeyResults.DoesNotExist) as e:
                raise APIError(message=INVALID_REQUEST, status=400)


class KeyResultsDetailsView(APIView):

    @send_api_response
    def put(self, request, keyresult_id):
        # TODO: check if user can create the task based on the information in header
        request_body = json.loads(request.body)
        try:
            keyresult_id = int(keyresult_id)
            title = str(request_body.get('title'))
            progress = int(request_body.get('progress'))
            keyresult = KeyResults.objects.get(pk=keyresult_id)
            if title:
                keyresult.title = title
            if progress:
                keyresult.progress = progress
            keyresult.save()
            return populate_keyresults_data(keyresult)
        except (ValueError, KeyResults.DoesNotExist, TypeError) as e:
            raise APIError(message=INVALID_REQUEST, status=400)

    @send_api_response
    def delete(self, request, keyresult_id):
        # TODO: check if user can create the task based on the information in header
        try:
            keyresult_id = int(keyresult_id)
            keyresult = KeyResults.objects.get(pk=keyresult_id)
            keyresult.is_discarded = True
            keyresult.save()
            return 'Keyresult successfully discarded'
        except (ValueError, KeyResults.DoesNotExist) as e:
            raise APIError(message=INVALID_REQUEST, status=400)
