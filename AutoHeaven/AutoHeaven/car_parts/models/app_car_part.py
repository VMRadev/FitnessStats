from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from AutoHeaven.car_parts.choices import CarPartChoices, CarStatusPartChoices

UserModel = get_user_model()


# class CarPartCategory(models.Model):
#     category = models.CharField(
#         max_length=30,
#         choices=CarPartChoices,
#         default=CarPartChoices.ENGINE,
#     )
#     quality = models.CharField(
#         max_length=30,
#         choices=CarStatusPartChoices,
#         default=CarStatusPartChoices.NEW,
#     )
#     quantity = models.PositiveIntegerField(
#         default=0,
#         validators=[MinValueValidator(0)],
#     )

# class Manufacturer(models.Model):
#     name = models.CharField(max_length=30)
#     rating = models.FloatField(
#         validators=[MinValueValidator(0), MaxValueValidator(5)],
#         default=0
#     )
#     type_parts = models.ManyToManyField(
#         to=CarPartCategory,
#         related_name="manufacturers",
#     )
#
#     def __str__(self):
#         return self.name


class CarPart(models.Model):
    owner = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )
    # category = models.ForeignKey(
    #     to=CarPartCategory,
    #     on_delete=models.CASCADE,
    # )
    name = models.CharField(
        max_length=50
    )
    description = models.CharField(
        max_length=120
    )
    price = models.DecimalField(
        decimal_places=2, max_digits=10
    )
    image = CloudinaryField('image', null=True, blank=True)
    # manufacturer = models.ForeignKey(
    #     to=Manufacturer,
    #     on_delete=models.CASCADE,
    # )

    def __str__(self):
        return self.name





