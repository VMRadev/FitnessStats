# Generated by Django 5.1.4 on 2024-12-11 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_carspecs_transmission_alter_carbrand_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carspecs',
            name='fuel_type',
            field=models.CharField(blank=True, choices=[('Electric', 'Electric'), ('Diesel', 'Diesel'), ('Petrol', 'Petrol')], default='Petrol', max_length=30, null=True),
        ),
    ]
