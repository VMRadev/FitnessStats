# Generated by Django 5.1.4 on 2024-12-11 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_car_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarSpecs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine', models.CharField(blank=True, max_length=30, null=True)),
                ('mileage', models.IntegerField(blank=True, null=True)),
                ('fuel_consumption', models.PositiveIntegerField(blank=True, null=True)),
                ('max_speed', models.IntegerField(blank=True, null=True)),
                ('fuel_type', models.CharField(blank=True, max_length=30, null=True)),
                ('max_distance', models.IntegerField(blank=True, null=True)),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
        ),
    ]
