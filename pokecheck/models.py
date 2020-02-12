from django.db import models


class Pokemon(models.Model):
    first_pick = models.CharField(max_length=60, default=None, blank=True)
    second_pick = models.CharField(max_length=60, default=None, blank=True)
