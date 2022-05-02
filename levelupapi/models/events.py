from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)