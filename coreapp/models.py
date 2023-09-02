from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

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
