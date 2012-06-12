from django.db import models

class Player(models.Model):
   name      = models.CharField(max_length=200)
   def __unicode__(self):
   	return self.name

class GameType(models.Model):
   name      = models.CharField(max_length=200)
   def __unicode__(self):
   	return self.name