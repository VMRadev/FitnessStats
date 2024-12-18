from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from AutoHeaven.cars.models import Car
from AutoHeaven.cars.models.app_car_specs import CarSpecs
from AutoHeaven.cars.tasks import notify_user_email, notify_user_deletion_car
from AutoHeaven.cars.utils import get_users_car_id


@receiver(post_save, sender=Car)
def create_car_specs(instance, created, **kwargs):
    if created:
        CarSpecs.objects.create(car=instance)
        users = get_users_car_id(instance.owner)
        for user in users:
            notify_user_email.delay(
                str(instance),
                str(user),
                user.email,
            )


@receiver(post_delete, sender=Car)
def delete_car_notify(sender, instance, **kwargs):
    users = get_users_car_id(instance.owner)
    for user in users:
        notify_user_deletion_car.delay(
            str(instance),
            str(user),
            user.email,
        )
