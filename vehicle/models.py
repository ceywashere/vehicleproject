from django.db import models


# Create your models here.

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    plaka = models.CharField(max_length=255)
    driver = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'
