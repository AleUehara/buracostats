#-*- coding: utf-8 -*-
from django import forms
from ..models import GameType

class GameTypeForm(forms.ModelForm):
    class Meta:
        model = GameType