import logging
from django.shortcuts import redirect
from django.urls import reverse

logger = logging.getLogger(__name__)

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

        # Allow access to admin and exempt paths
        if request.path.startswith('/admin/') or request.path in exempt_paths:
            return None

        if request.user.is_authenticated:
            # If the user does not have a role assigned
            if not (request.user.is_trainer or request.user.is_manager or request.user.is_temp_manager):
                if request.path != reverse('set_account_role'):
                    return redirect('set_account_role')

            # If the user is a manager
            if request.user.is_manager:
                # Only redirect to manager dashboard if they are accessing the dashboard URL
                if request.path == reverse('manager_dashboard'):
                    return None  # Allow access to the manager dashboard
                # Allow access to other manager-related URLs without redirecting

            # If the user is a temporary manager waiting for authentication
            if request.user.is_temp_manager:
                # Only redirect to manager dashboard if they are accessing the dashboard URL
                if request.path == reverse('authenticate_manager'):
                    return None  # Allow access to the manager dashboard
                # Allow access to other manager-related URLs without redirecting

            # If the user is a trainer
            if request.user.is_trainer:
                # Only redirect to trainer dashboard if they are accessing the dashboard URL
                if request.path == reverse('trainer_dashboard'):
                    return None  # Allow access to the trainer dashboard
                # Allow access to other trainer-related URLs without redirecting

        return None  # No redirection needed
