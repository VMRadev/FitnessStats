# Generated by Django 5.1.4 on 2024-12-16 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_alter_carspecs_fuel_consumption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carspecs',
            name='id',
        ),
        migrations.AlterField(
            model_name='carspecs',
            name='car',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='specs', serialize=False, to='cars.car'),
        ),
    ]
