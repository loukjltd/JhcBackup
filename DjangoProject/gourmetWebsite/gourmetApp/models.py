from django.db import models


# Create your models here.
class Dishes(models.Model):
    dish_name = models.CharField(max_length=30, primary_key=True)
    price = models.IntegerField()
    rate = models.DecimalField(decimal_places=1, max_digits=2)


class Material(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    calory = models.IntegerField()
    price = models.FloatField()


class User(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
