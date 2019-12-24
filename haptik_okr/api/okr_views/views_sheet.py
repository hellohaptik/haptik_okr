from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from api.exceptions import APIError
import api.constants
from api.models.okr_related import Objective, KeyResults
from api.okr_decorators import send_api_response
import json


def get_sheet_details(sheet_id):
    response = {}
    okrs = []
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


class SheetView(APIView):
    @method_decorator(send_api_response)
    def get(self, request):
        request_params = request.query_params.dict()
        if len(request_params) > 0:
            try:
                if request_params.get('id') is not None:
                    sheet_id = int(request_params.get('id'))
                    return get_sheet_details(sheet_id)
                else:
                    raise APIError(api.constants.INVALID_REQUEST, status=400)
            except ValueError as e:
                raise APIError(message="Invalid id", status=400)
        else:
            raise APIError(message=api.constants.INVALID_REQUEST, status=400)


class SheetDetailView(APIView):

    @method_decorator(send_api_response)
    def put(self, request, sheet_id):
        try:
            # cast the sheet_id to int else raise an exception
            s_id = int(sheet_id)

            # get objectives and keyresults data from db for validations
            db_objective_list = Objective.objects.filter(quarter_sheet_id=s_id)
            db_objective_id_list = [objective.id for objective in db_objective_list]
            db_keyresults_list = KeyResults.objects.filter(objective__id__in=db_objective_id_list)

            # parse the request body into dict
            request_body = json.loads(request.body)

            # get the list of objectives from the request body
            req_objective_list = request_body.get('objectives')
            if req_objective_list:
                valid_objectives_keyresults = self.validate_objectives_and_keyresults(req_objective_list,
                                                                                      db_objective_id_list,
                                                                                      db_keyresults_list)
                if valid_objectives_keyresults:
                    self.update_objectives_and_keyresults(req_objective_list, db_objective_list, db_keyresults_list)
                    return get_sheet_details(s_id)
                else:
                    raise APIError(message="Invalid data", status=400)
            return "Return a sheet object with updated data of objectives and keyresults"
        except ValueError as e:
            raise APIError(message="Invalid sheet id", status=400)

    def validate_objectives_and_keyresults(self, req_objective_list, db_objective_id_list, db_keyresults_list):
        for req_objective in req_objective_list:
            # check if the objective in the request belongs to the sheet id sent in the url
            if req_objective.get('id') not in db_objective_id_list:
                return False
            else:
                objective_id = req_objective.get('id')
                # get the ids of keyresults for the objective in the request from the db
                obj_keyresults_ids = db_keyresults_list.filter(objective_id=objective_id).values_list('id', flat=True)
                # get the keyresults from the request objective object
                req_obj_keyresults = req_objective.get('keyresults')
                # check if the keyresults sent as a part of the objective in the request belong to the objective
                for req_obj_keyresult in req_obj_keyresults:
                    if req_obj_keyresult.get('id') not in obj_keyresults_ids:
                        return False
        return True

    def update_objectives_and_keyresults(self, req_objective_list, db_objective_list, db_keyresults_list):
        for req_objective in req_objective_list:

            # update the objective object
            db_objective = db_objective_list.get(pk=req_objective.get('id'))
            db_objective.title = req_objective.get('title')
            db_objective.save()

            # update the keyresults for the objective
            req_keyresults_list = req_objective.get('keyresults')
            for req_keyresult in req_keyresults_list:
                db_keyresult = db_keyresults_list.get(pk=req_keyresult.get('id'))

                # update the data for db keyresult
                db_keyresult.title = req_keyresult.get('title')
                db_keyresult.progress = req_keyresult.get('progress')
                db_keyresult.objective = db_objective
                db_keyresult.save()
