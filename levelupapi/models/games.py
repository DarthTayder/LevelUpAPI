from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User




class Games(models.Model):

    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    number_of_players = models.DecimalField(max_length=7, decimal_places=2)
    skill_level = models.CharField(max_length=50)