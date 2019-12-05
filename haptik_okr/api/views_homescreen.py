import json
from django.http import HttpResponse
from rest_framework.views import APIView
from api.models.okr_related import Quarter


def populate_quarter_data(quarter_list):
    all_quarter_data = []
    if len(quarter_list) == 1:
        data = {
            'id': quarter_list[0].id,
            'name': quarter_list[0].quarter_name,
            'quarter_start_date': quarter_list[0].quarter_start_date.strftime('%m/%d/%Y'),
            'quarter_end_date': quarter_list[0].quarter_end_date.strftime('%m/%d/%Y'),
            'is_current': quarter_list[0].is_current
        }

        return data

    for quarter in quarter_list:
        data = {
            'id': quarter.id,
            'name': quarter.quarter_name,
            'quarter_start_date': quarter.quarter_start_date.strftime('%d/%m/%Y'),
            'quarter_end_date': quarter.quarter_end_date.strftime('%d/%m/%Y'),
            'is_current': quarter.is_current
        }
        all_quarter_data.append(data)
    return all_quarter_data


class QuarterView(APIView):

    def get(self, request):
        quarter_list = []
        request_params = request.query_params.dict()
        if len(request_params) > 0:
            if request_params.get('is_current') is not None:
                is_current = request_params.get('is_current')
                if str.lower(is_current) == 'true':
                    quarter_list = Quarter.objects.filter(is_current=True).order_by('quarter_start_date')
                elif str.lower(is_current) == 'false':
                    quarter_list = Quarter.objects.filter(is_current=False)
            else:
                return HttpResponse("Invalid request")
        else:
            quarter_list = Quarter.objects.all()

        return HttpResponse(json.dumps(populate_quarter_data(quarter_list)))
