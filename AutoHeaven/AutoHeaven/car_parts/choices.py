from django.db import models


class CarPartChoices(models.TextChoices):
    ENGINE = 'ENGINE', 'Engine'
    TRANSMISSION = 'TRANSMISSION', 'Transmission'
    BRAKES = 'BRAKES', 'Brakes'
    SUSPENSION = 'SUSPENSION', 'Suspension'
    WHEELS = 'WHEELS', 'Wheels'
    BATTERY = 'BATTERY', 'Battery'
    EXHAUST = 'EXHAUST', 'Exhaust'
    AIR_FILTER = 'AIR_FILTER', 'Air Filter'
    FUEL_TANK = 'FUEL_TANK', 'Fuel Tank'

class CarStatusPartChoices(models.TextChoices):
    USED = 'Used', 'Used'
    NEW = 'New', 'New'
    DAMAGED = 'Damaged', 'Damaged'
    REFURBISHED = 'Refurbished', 'Refurbished'