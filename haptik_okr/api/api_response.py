from django.http import HttpResponse
import json


class ApiResponse(object):
    def __init__(self):
        self.success = False
        self.body = {}
        self.error = ''
        self.status_code = 200

    def toHttpResponse(self):
        """
        Generates a HttpResponse object with data in the specific response format
        and status_code as 200
        """
        body = {'success': self.success, 'body': self.body, 'status_code': self.status_code, 'error': self.error}
        return HttpResponse(json.dumps(body), content_type="application/json", status=self.status_code)
