from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FitnessStats.accounts'


    def ready(self):
        import FitnessStats.accounts.signals
