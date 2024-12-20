# Generated by Django 5.1.4 on 2024-12-11 09:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_car_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='car',
            name='model',
        ),
        migrations.AlterField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='car',
            name='brand',
            field=models.ManyToManyField(related_name='car', to='cars.carbrand'),
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ManyToManyField(related_name='car', to='cars.carmodel'),
        ),
    ]
