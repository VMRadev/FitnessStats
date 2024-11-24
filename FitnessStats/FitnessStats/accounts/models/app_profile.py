from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
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

    weight = models.PositiveSmallIntegerField(
        default=0,
        blank=True,
        null=True,
    )

    height = models.PositiveSmallIntegerField(
        default=0,
        blank=True,
        null=True,
    )

    deadlift = models.PositiveSmallIntegerField(
        default=0,
        blank=True,
        null=True,
    )

    bench = models.PositiveSmallIntegerField(
        default=0,
        blank=True,
        null=True,
    )

    squat = models.PositiveSmallIntegerField(
        default=0,
        blank=True,
        null=True,
    )

    def total(self):
        return self.deadlift + self.bench + self.squat

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def body_strength_percentage(self):
        if self.deadlift > 0 and self.bench > 0 and self.squat > 0 and self.weight > 0:
            return {
                'deadlift': self.deadlift / self.weight,
                'bench': self.bench / self.weight,
                'squat': self.squat / self.weight,
            }

    def __str__(self):
        return f'{self.total()}'
