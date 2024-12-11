# Generated by Django 5.1.4 on 2024-12-11 09:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_carmodel_brand_remove_car_brand_remove_car_model_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to=settings.AUTH_USER_MODEL),
        ),
    ]
