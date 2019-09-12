from django.conf import settings
from django.db import models
from django.utils import timezone


class Flower(models.Model):
    id = models.IntegerField(primary_key=True)
    categories = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=16)

    def __str__(self):
        return self.categories

class Gift(models.Model):
    id = models.IntegerField(primary_key=True)
    categories = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=16)

    def __str__(self):
        return self.categories
