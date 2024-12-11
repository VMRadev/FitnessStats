from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AutoHeaven.accounts'


    def ready(self):
        import AutoHeaven.accounts.signals