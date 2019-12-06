from rest_framework.decorators import api_view
from api.models.okr_related import Quarter
from api.okr_decorators import send_api_response
from api.exceptions import APIError
import datetime


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
                try:
                    is_current = int(request_params.get('is_current'))
                    if is_current == 1:
                        quarter_list = Quarter.objects.filter(is_current=True).order_by('quarter_start_date')
                    elif is_current == 0:
                        quarter_list = Quarter.objects.filter(is_current=False)
                except ValueError as e:
                    raise APIError(message='Invalid Request', status=400)
            elif request_params.get('all') is not None:
                all_quarters = int(request_params.get('all'))
                if all_quarters == 1:
                    quarter_list = Quarter.objects.all()
        except ValueError as e:
            raise APIError(message='Invalid Request', status=400)
    else:
        raise APIError(message='Invalid Request', status=400)

    return populate_quarter_data(quarter_list)


@api_view()
@send_api_response
def get_quarter_by_id(request, quarter_id):
    print(quarter_id)
    try:
        q_id = int(quarter_id)
        if q_id < 0:
            raise APIError(message='Invalid Id', status=400)
        else:
            quarter_list = Quarter.objects.filter(id=q_id)
            return populate_quarter_data(quarter_list)

    except ValueError as e:
        raise APIError(message='Quarter id should be an integer', status=400)
