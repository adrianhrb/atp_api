from django.db import models


class Hand(models.TextChoices):
    RIGHT = 'R', 'right'
    LEFT = 'L', 'left'


class Player(models.Model):
    name = models.CharField(max_length=255)
    hand = models.CharField(choices=Hand, max_length=1)
    country = models.CharField(max_length=3)
    birthdate = models.DateField(blank=True)
