#-*- coding: utf-8 -*-
from django import forms

class FormPlayer(forms.Form):
  name = forms.CharField(max_length=100)
