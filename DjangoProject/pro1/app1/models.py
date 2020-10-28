from django.db import models


class Dishes(models.Model):
    dish_name = models.CharField(max_length=20)
    price = models.IntegerField()
    rate = models.DecimalField(decimal_places=1, max_digits=1)


class Material(models.Model):
    dish_name = models.CharField(max_length=25)
    material1 = models.CharField(max_length=25)
    material2 = models.CharField(max_length=25)
    material3 = models.CharField(max_length=25)

