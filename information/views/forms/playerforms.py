#-*- coding: utf-8 -*-
from django import forms
from ..models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player