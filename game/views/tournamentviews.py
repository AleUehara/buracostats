#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from ..forms import TournamentForm
from django.template import RequestContext
from ..models import Tournament

def tournament(request):
	values = Tournament.objects.all()
	return render_to_response("tournamentlist.html", {'values': values})

def addtournament(request):
    form = TournamentForm(request.POST or None)
    if form.is_valid():
        mymodel = form.save()
        mymodel.added_at_djangocon = True
        mymodel.save()
        return tournament(request)
    return render_to_response("add.html", {'form' : form}, context_instance=RequestContext(request))

def deletetournament(request, id):    
    u = Tournament.objects.get(pk=id).delete()
    values = Tournament.objects.all()
    return render_to_response("tournamentlist.html", {'values': values})
