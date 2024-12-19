from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models

from AutoHeaven.cars.choices import CarTransmissionType

UserModel = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile',
    )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    height = models.PositiveSmallIntegerField(
        default=0,
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    preferred_transmission = models.CharField(
        choices=CarTransmissionType,
        blank=True,
        null=True,
    )

    image = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        full_name = f"{self.first_name or ''} {self.last_name or ''}".strip()
        return full_name if full_name else self.user.username
