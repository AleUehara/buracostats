from django.db import models
from information.models import Player
from information.models import GameType
from information.models import WinnerPoints

class Tournament(models.Model):
   game_type              = models.ForeignKey(GameType)
   date                   = models.DateField()
   players_first_team     = models.ManyToManyField(Player, related_name="First Team")
   players_second_team    = models.ManyToManyField(Player, related_name="Second Team")
   winner_points          = models.ForeignKey(WinnerPoints)
   
   def __unicode__(self):
     first_team_players  = self.concat_players(self.players_first_team.all())
     second_team_players = self.concat_players(self.players_second_team.all())

     return '%s - %s vs %s' % (self.date.strftime("%d/%m/%y"), first_team_players, second_team_players )

   def concat_players(self, team):
     team_players = []
     for player in team:
       team_players.append(player.name)
     team_players = '/'.join(team_players)
     return team_players
