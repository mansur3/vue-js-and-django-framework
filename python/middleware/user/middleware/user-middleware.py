from django.utils.deprecation import MiddlewareMixin
import json

class UserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        
        print('requestfirst', request.body, request.headers)
        return None
    def process_response(self, request, response):
        

        print('then ==============================>>>>>>>>>>>>')
        print('request', request.body, request.headers)
        print('response', response.data)
        return response