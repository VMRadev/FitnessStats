# Generated by Django 5.1.4 on 2024-12-10 16:39

import cloudinary.models
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Coupe', 'Coupe'), ('Convertible', 'Convertible'), ('Hatchback', 'Hatchback'), ('Wagon', 'Wagon'), ('Pickup', 'Pickup Truck'), ('Minivan', 'Minivan'), ('Van', 'Van'), ('SportsCar', 'Sports Car'), ('Crossover', 'Crossover'), ('Luxury', 'Luxury'), ('OffRoad', 'Off-Road'), ('Compact', 'Compact'), ('Subcompact', 'Subcompact'), ('Roadster', 'Roadster')], default='Sedan', max_length=30)),
                ('status', models.CharField(choices=[('Used', 'Used'), ('New', 'New'), ('Damaged', 'Damaged')], default='Used', max_length=30)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2024)])),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carbrand')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carmodel')),
            ],
        ),
    ]
