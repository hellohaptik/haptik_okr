from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from api.exceptions import APIError
import api.constants
from api.models.okr_related import Objective, KeyResults
from api.okr_decorators import send_api_response


class SheetView(APIView):

    @method_decorator(send_api_response)
    def get(self, request):
        request_params = request.query_params.dict()
        response = {}
        okrs = []
        if len(request_params) > 0:
            try:
                if request_params.get('id') is not None:
                    sheet_id = int(request_params.get('id'))
                    objective_list = Objective.objects.filter(quarter_sheet_id=sheet_id)
                    objective_id_list = [objective.id for objective in objective_list]
                    keyresults_list = KeyResults.objects.filter(objective__id__in=objective_id_list)
                    for obj in objective_list:
                        krs = []
                        for kr in keyresults_list.filter(objective_id=obj.id):
                            keyresult = {
                                'id': kr.id,
                                'title': kr.title,
                                'progress': kr.progress,
                                'is_discarded': kr.is_discarded
                            }
                            krs.append(keyresult)
                        objective = {
                            'id': obj.id,
                            'title': obj.title,
                            'progress': obj.progress,
                            'keyresults': krs}
                        okrs.append(objective)
                        response['objectives'] = okrs
                    return response
                else:
                    raise APIError(api.constants.INVALID_REQUEST, status=400)
            except ValueError as e:
                raise APIError(message="Invalid id", status=400)
        else:
            raise APIError(message=api.constants.INVALID_REQUEST, status=400)


class SheetDetailView(APIView):

    @method_decorator(send_api_response)
    def put(self, request, sheet_id):
        pass
