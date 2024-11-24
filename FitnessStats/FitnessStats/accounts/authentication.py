from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailOrUsernameBackend(ModelBackend):
    """
    Custom authentication backend to allow login with email or username.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Check if user exists with either email or username
        try:
            user = User.objects.get(
                username=username
            ) if User.objects.filter(username=username).exists() else User.objects.get(email=username)
        except User.DoesNotExist:
            return None

        # Check the password
        if user.check_password(password):
            return user

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
