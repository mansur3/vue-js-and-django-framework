from typing import Any


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        response = self.get_response(request)
        print("welcome to the another world")
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        # This code is executed just before the view is called
        print('welcome to the world')
        return request

    def process_exception(self, request, exception):
        # This code is executed if an exception is raised
        print("Welcome to the another world.")

    def process_template_response(self, request, response):
        # This code is executed if the response contains a render() method
        return response
