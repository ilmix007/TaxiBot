from django.contrib.gis.geos import Point
from django.db import models


class Driver(models.Model):
    """Водитель"""
    user = models.ForeignKey('coreapp.CustomUser', on_delete=models.CASCADE)
    location = Point
    in_waiting = models.BooleanField(default=False)
    on_the_route = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    """Заказчик"""
    user = models.ForeignKey('coreapp.CustomUser', on_delete=models.CASCADE)
    location = Point
    in_waiting = models.BooleanField(default=False)
    on_the_route = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)


class Order(models.Model):
    """Заказ"""
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    from_location = Point
    to_location = Point
    is_active = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
