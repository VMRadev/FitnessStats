from django.db import models


class CarTypeChoices(models.TextChoices):
    SEDAN = 'Sedan', 'Sedan'
    SUV = 'SUV', 'SUV'
    COUPE = 'Coupe', 'Coupe'
    CONVERTIBLE = 'Convertible', 'Convertible'
    HATCHBACK = 'Hatchback', 'Hatchback'
    WAGON = 'Wagon', 'Wagon'
    PICKUP_TRUCK = 'Pickup', 'Pickup Truck'
    MINIVAN = 'Minivan', 'Minivan'
    VAN = 'Van', 'Van'
    SPORTS_CAR = 'SportsCar', 'Sports Car'
    CROSSOVER = 'Crossover', 'Crossover'
    LUXURY = 'Luxury', 'Luxury'
    OFF_ROAD = 'OffRoad', 'Off-Road'
    COMPACT = 'Compact', 'Compact'
    SUBCOMPACT = 'Subcompact', 'Subcompact'
    ROADSTER = 'Roadster', 'Roadster'

class CarStatusChoices(models.TextChoices):
    USED = 'Used', 'Used'
    NEW = 'New', 'New'
    DAMAGED = 'Damaged', 'Damaged'

class CarTypeFuelChoices(models.TextChoices):
    ELECTRIC = 'Electric', 'Electric'
    DIESEL = 'Diesel', 'Diesel'
    PETROL = 'Petrol', 'Petrol'

class CarTransmissionType(models.TextChoices):
    AUTOMATIC = 'Automatic', 'Automatic'
    MANUAL = 'Manual', 'Manual'
