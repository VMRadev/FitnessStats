# Generated by Django 5.1.4 on 2024-12-11 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_carspecs_description_alter_carspecs_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='carspecs',
            name='transmission',
            field=models.CharField(blank=True, choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')], default='Manual', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='carbrand',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='model',
            field=models.CharField(max_length=30),
        ),
    ]
