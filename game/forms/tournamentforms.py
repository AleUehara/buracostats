#-*- coding: utf-8 -*-
from django import forms
from ..models import Tournament

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament