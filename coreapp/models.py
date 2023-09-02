from django.db import models


class Bot(models.Model):
    """Бот"""
    token = models.CharField(verbose_name='Token', max_length=63)
    name = models.CharField(verbose_name='Name', max_length=63)
    about = models.TextField(verbose_name='About', max_length=255)
    description = models.TextField(verbose_name='Description', max_length=255)
