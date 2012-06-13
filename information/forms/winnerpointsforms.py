#-*- coding: utf-8 -*-
from django import forms
from information.models import WinnerPoints

class WinnerPointsForm(forms.ModelForm):
    class Meta:
        model = WinnerPoints