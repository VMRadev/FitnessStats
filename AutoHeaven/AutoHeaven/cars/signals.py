from django.db.models.signals import post_save
from django.dispatch import receiver
from AutoHeaven.cars.models import Car
from AutoHeaven.cars.models.app_car_specs import CarSpecs


@receiver(post_save, sender=Car)
def create_car_specs(instance, created, **kwargs):
    if created:
        CarSpecs.objects.create(car=instance)