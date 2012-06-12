from django.contrib import admin
from information.models import Player
from django import forms


#class CorporateEmailForm(forms.ModelForm):
#    password = forms.CharField(widget=PasswordInput())


#class CorporateEmailAdmin(admin.ModelAdmin):
#    form = CorporateEmailForm

admin.site.register(Player)
#admin.site.register(User)
#admin.site.register(CorporateEmail, CorporateEmailAdmin)

