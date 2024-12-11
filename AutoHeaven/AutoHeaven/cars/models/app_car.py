from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from AutoHeaven.cars.choices import CarTypeChoices, CarStatusChoices

UserModel = get_user_model()

class CarBrand(models.Model):
    name = models.CharField(
        max_length=30,
    )

    def __str__(self):
        return self.name

class CarModel(models.Model):
    model = models.CharField(
        max_length=30,
    )
    brand = models.ForeignKey(
        to=CarBrand,
        on_delete=models.CASCADE,
        related_name='model',
    )

    def __str__(self):
        return self.model

# Create your models here.
class Car(models.Model):
    owner = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='car',
    )
    brand = models.ForeignKey(
        to=CarBrand,
        on_delete=models.CASCADE,
        related_name='car',
    )
    model = models.ForeignKey(
        to=CarModel,
        on_delete=models.CASCADE,
        related_name='car',
    )
    price = models.IntegerField()
    color = models.CharField(
        max_length=30
    )
    type = models.CharField(
        max_length=30,
        choices=CarTypeChoices,
        default=CarTypeChoices.SEDAN
    )
    status = models.CharField(
        max_length=30,
        choices=CarStatusChoices,
        default=CarStatusChoices.USED
    )
    year = models.IntegerField(
        validators=[MinValueValidator(1950), MaxValueValidator(2024)],
    )
    image = CloudinaryField('image')

    def __str__(self):
        return f'{self.brand} {self.model}'
