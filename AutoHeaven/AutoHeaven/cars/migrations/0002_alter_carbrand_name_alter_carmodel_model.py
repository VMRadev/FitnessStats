# Generated by Django 5.1.4 on 2024-12-10 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carbrand',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='model',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
