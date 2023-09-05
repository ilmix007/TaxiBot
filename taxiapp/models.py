from django.contrib import admin
from django.contrib.gis.geos import Point
from django.db import models


class Driver(models.Model):
    """Водитель"""
    user = models.ForeignKey('coreapp.CustomUser', on_delete=models.CASCADE)

    @property
    @admin.display(ordering="user", )
    def loc(self):
        return f'{self.user.location.x}, {self.user.location.y}'

    @property
    @admin.display(ordering="in_waiting", )
    def in_waiting(self):
        return self.user.in_waiting

    @property
    @admin.display(ordering="on_the_route", )
    def on_the_route(self):
        return self.user.on_the_route


class Customer(models.Model):
    """Заказчик"""
    user = models.ForeignKey('coreapp.CustomUser', on_delete=models.CASCADE)

    @property
    @admin.display(ordering="user")
    def loc(self):
        return f'{self.user.location.x}, {self.user.location.y}'

    @property
    @admin.display(ordering="in_waiting")
    def in_waiting(self):
        return self.user.in_waiting

    @property
    @admin.display(ordering="on_the_route")
    def on_the_route(self):
        return self.user.on_the_route


class Order(models.Model):
    """Заказ"""
    customer = models.ForeignKey(Customer,
                                 verbose_name='Customer',
                                 on_delete=models.CASCADE,
                                 related_name='orders')
    driver = models.ForeignKey(Driver,
                               verbose_name='Driver',
                               on_delete=models.CASCADE,
                               related_name='calls',
                               blank=True, null=True)
    from_location = Point
    to_location = Point
    is_active = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
