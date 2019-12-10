from rest_framework.decorators import api_view
from api.models.okr_related import Quarter, Sheet, Team
from api.okr_decorators import send_api_response
from api.exceptions import APIError
import datetime
import api.constants


def populate_quarter_data(quarter_list):
    all_quarter_data = []
    response = {'quarters': None}
    for quarter in quarter_list:
        if quarter.quarter_start_date < datetime.date.today():
            data = {
                'id': quarter.id,
                'name': quarter.quarter_name,
                'quarter_start_date': quarter.quarter_start_date.strftime('%d/%m/%Y'),
                'quarter_end_date': quarter.quarter_end_date.strftime('%d/%m/%Y'),
                'is_current': quarter.is_current
            }
            all_quarter_data.append(data)
    response['quarters'] = all_quarter_data
    return response


@api_view()
@send_api_response
def get_all_or_current_quarter(request):
    quarter_list = []
    request_params = request.query_params.dict()
    if len(request_params) > 0:
        try:
            if request_params.get('is_current') is not None:
                is_current = int(request_params.get('is_current'))
                if is_current == 1:
                    quarter_list = Quarter.objects.filter(is_current=True).order_by('quarter_start_date')
                elif is_current == 0:
                    quarter_list = Quarter.objects.filter(is_current=False)
                else:
                    raise APIError(message=api.constants.INVALID_REQUEST, status=400)
            else:
                raise APIError(message=api.constants.INVALID_REQUEST, status=400)
        except ValueError as e:
            raise APIError(message=api.constants.INVALID_REQUEST, status=400)
    else:
        quarter_list = Quarter.objects.all()

    return populate_quarter_data(quarter_list)


@api_view()
@send_api_response
def get_quarter_by_id(request, quarter_id):
    try:
        q_id = int(quarter_id)
        if q_id < 0:
            raise APIError(message='Invalid Id', status=400)
        else:
            quarter_list = Quarter.objects.filter(id=q_id)
            return populate_quarter_data(quarter_list)

    except ValueError as e:
        raise APIError(message='Quarter id should be an integer', status=400)


@api_view()
@send_api_response
def get_team_list_for_quarter_id(request, quarter_id):
    response = {'teams_progress': None}
    teams_progress = []
    try:
        q_id = int(quarter_id)
        sheet_list = Sheet.objects.filter(quarter_id_id=q_id).select_related('team_id')
        for sheet in sheet_list:
            data = {
                'sheet_id': sheet.id,
                'team_name': sheet.team_id.name,
                'team_progress': sheet.progress
            }
            teams_progress.append(data)
        response['teams_progress'] = teams_progress
        return response
    except ValueError as e:
        raise APIError(message="Invalid quarter id", status=400)
