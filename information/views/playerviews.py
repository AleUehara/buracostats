#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from information.forms import PlayerForm
from django.template import RequestContext
from information.models import Player

def player(request):
	values = Player.objects.all()
	return render_to_response("playerlist.html", {'values': values})

def addplayer(request):
    form = PlayerForm(request.POST or None)
    if form.is_valid():
        mymodel = form.save()
        mymodel.added_at_djangocon = True
        mymodel.save()
        return player(request)
    return render_to_response("add.html", {'form' : form}, context_instance=RequestContext(request))

def deleteplayer(request, id):    
    u = Player.objects.get(pk=id).delete()
    values = Player.objects.all()
    return render_to_response("playerlist.html", {'values': values})
