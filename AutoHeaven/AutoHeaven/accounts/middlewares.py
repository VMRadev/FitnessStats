from django.shortcuts import redirect
from django.conf import settings


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and not request.path.startswith(settings.LOGIN_URL):
            # Exclude static files, admin, or specific paths
            if not any(request.path.startswith(path) for path in settings.LOGIN_EXEMPT_URLS):
                return redirect(f"{settings.LOGIN_URL}?next={request.path}")
        return self.get_response(request)
