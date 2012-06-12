from django.db import models
from information.models import Player
from information.models import GameType

class Tournament(models.Model):
   game_type              = models.ForeignKey(GameType)
   date                   = models.DateField()
   players_first_team     = models.ManyToManyField(Player, related_name="First Team")
   players_second_team    = models.ManyToManyField(Player, related_name="Second Team")
   def __unicode__(self):
   	return self.date

