from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AutoHeaven.cars'

    def ready(self):
        import AutoHeaven.cars.signals
