# Generated by Django 5.1.3 on 2024-11-18 13:02

import AutoHeaven.accounts.managers
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appaccount',
            options={},
        ),
        migrations.AlterModelManagers(
            name='appaccount',
            managers=[
                ('objects', AutoHeaven.accounts.managers.AppUserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='appaccount',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='appaccount',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='appaccount',
            name='last_name',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('weight', models.PositiveSmallIntegerField(default=0)),
                ('height', models.PositiveSmallIntegerField(default=0)),
                ('deadlift', models.PositiveSmallIntegerField(default=0)),
                ('bench', models.PositiveSmallIntegerField(default=0)),
                ('squat', models.PositiveSmallIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]