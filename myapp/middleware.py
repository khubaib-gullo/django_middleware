from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden

from mysite import settings

class IpBlocker:
    def __init__(self, get_response):

        self.get_response = get_response
        print(get_response)
        # One-time configuration and initialization.

    def __call__(self, request):
        # blocking ip by port no
        
        # add = request.META['REMOTE_ADDR']+":"+request.META['SERVER_PORT']+request.META['PATH_INFO']
        # print(add)
        # if add == "127.0.0.1:8000/home/":
        #     raise PermissionDenied()
        # response = self.get_response(request)
        
        # bloking ip by adding list of bannedips in  settings.py file
        
        # if hasattr(settings, 'BANNED_IPS') and settings.BANNED_IPS is not None:
        #     if request.META['REMOTE_ADDR'] in settings.BANNED_IPS:
        #         raise PermissionDenied()
        response = self.get_response(request)
        return response


    def process_view(self, request, view_func, view_args, view_kwargs):
        # Check if the user is blocked
       # print(type(request.user))
       # print(type(view_func.__name__))
        if request.user.username == 'jhon' and view_func.__name__ == "home":
            return HttpResponseForbidden("You are currently blocked from accessing this application.")

        # Pass through if not blocked
        return None  # Allow processing by the view


