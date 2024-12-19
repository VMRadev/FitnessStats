from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class CarPart(models.Model):
    owner = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )
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

    def __str__(self):
        return self.name





