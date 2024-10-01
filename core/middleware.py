from django.shortcuts import redirect
from django.urls import reverse

class BaseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.process_request(request)
        if response:
            return response
        response = self.get_response(request)
        return self.process_response(request, response)

    def process_request(self, request):
        return None

    def process_response(self, request, response):
        return response


class RoleRedirectMiddleware(BaseMiddleware):
    def process_request(self, request):
        exempt_paths = [
            reverse('set_account_role'),
            reverse('login'),
            reverse('logout'),
        ]

        # Exempt the admin path
        if request.path.startswith('/admin/') or request.path in exempt_paths :
            return None

        # Check user roles and redirect accordingly
        if request.user.is_authenticated:
            if request.user.is_trainer:
                if request.path != reverse('trainer_dashboard'):
                    return redirect('trainer_dashboard')
            elif request.user.is_manager:
                if request.path != reverse('manager_dashboard'):
                    return redirect('manager_dashboard')
            else:  # No role assigned
                if request.path != reverse('set_account_role'):
                    return redirect('set_account_role')

        return None
