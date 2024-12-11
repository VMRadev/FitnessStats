# Generated by Django 5.1.4 on 2024-12-11 09:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_remove_car_brand_remove_car_model_alter_car_owner_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='model', to='cars.carbrand'),
            preserve_default=False,
        ),
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
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='car', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='car', to='cars.carbrand'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='car', to='cars.carmodel'),
            preserve_default=False,
        ),
    ]
