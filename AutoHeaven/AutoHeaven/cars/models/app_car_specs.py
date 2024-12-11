from django.core.validators import MinValueValidator
from django.db import models

from AutoHeaven.cars.choices import CarTransmissionType, CarTypeFuelChoices
from AutoHeaven.cars.models.app_car import Car


class CarSpecs(models.Model):
    car = models.OneToOneField(
        to=Car,
        on_delete=models.CASCADE,
        related_name='specs',
    )
    engine = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )
    mileage = models.IntegerField(
        blank=True,
        null=True
    )
    fuel_consumption = models.DecimalField(
        validators=[MinValueValidator(0)],
        max_digits=3,
        decimal_places=2,
        blank=True,
        null=True
    )
    max_speed = models.IntegerField(
        blank=True,
        null=True
    )
    fuel_type = models.CharField(
        max_length=30,
        choices=CarTypeFuelChoices,
        default=CarTypeFuelChoices.PETROL,
        blank=True,
        null=True
    )
    max_distance = models.IntegerField(
        blank=True,
        null=True
    )
    transmission = models.CharField(
        max_length=30,
        choices=CarTransmissionType,
        default=CarTransmissionType.MANUAL,
        blank=True,
        null=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.car)