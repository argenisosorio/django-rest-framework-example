# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Serie(models.Model):
    """
    Crearemos un modelo llamado Serie, dentro de nuestra app series, el cual
    representará toda la información que posee una serie de TV.
    """
    HORROR = 'horror'
    COMEDY = 'comedy'
    ACTION = 'action'
    DRAMA = 'drama'

    CATEGORIES_CHOICES = (
        (HORROR, 'Horror'),
        (COMEDY, 'Comedy'),
        (ACTION, 'Action'),
        (DRAMA, 'Drama'),
    )

    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(default=0)
    category = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)

    def __unicode__(self):
        return self.name