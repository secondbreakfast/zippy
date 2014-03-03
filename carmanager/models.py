from django.db import models

class Car(models.Model):
    year = models.IntegerField(max_length=4)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    horsepower = models.IntegerField(max_length=3)
    transmission = models.CharField(max_length=50)
    gears = models.CharField(max_length=50)


# Create your models here.
