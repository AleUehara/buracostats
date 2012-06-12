#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from ..forms import GameTypeForm
from django.template import RequestContext
from ..models import GameType

def gametype(request):
	values = GameType.objects.all()
	return render_to_response("gametypelist.html", {'values': values})

def addgametype(request):
    form = GameTypeForm(request.POST or None)
    if form.is_valid():
        mymodel = form.save()
        mymodel.added_at_djangocon = True
        mymodel.save()
        return gametype(request)
    return render_to_response("add.html", {'form' : form}, context_instance=RequestContext(request))

def deletegametype(request, id):    
    u = GameType.objects.get(pk=id).delete()
    values = GameType.objects.all()
    return render_to_response("gametypelist.html", {'values': values})
