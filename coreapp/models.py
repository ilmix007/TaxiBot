from django.contrib.auth.models import AbstractUser
from django.contrib.gis.geos import Point
from django.db import models
from django.contrib.gis.db import models


class CustomUser(AbstractUser):
    tg_id = models.CharField(max_length=63, blank=True, null=True)
    location = models.PointField(blank=True, null=True)
    in_waiting = models.BooleanField(default=False)
    on_the_route = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Bot(models.Model):
    """Бот"""
    token = models.CharField(verbose_name='Token', max_length=63, unique=True)
    name = models.CharField(verbose_name='Name', max_length=63)
    about = models.TextField(verbose_name='About', max_length=255,
                             null=True, blank=True)
    description = models.TextField(verbose_name='Description', max_length=255,
                                   null=True, blank=True)
