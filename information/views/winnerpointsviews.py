#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from information.forms import WinnerPointsForm
from django.template import RequestContext
from information.models import WinnerPoints

def winnerpoints(request):
	values = WinnerPoints.objects.all()
	return render_to_response("winnerpointslist.html", {'values': values})

def addwinnerpoints(request):
    form = WinnerPointsForm(request.POST or None)
    if form.is_valid():
        mymodel = form.save()
        mymodel.added_at_djangocon = True
        mymodel.save()
        return winnerpoints(request)
    return render_to_response("add.html", {'form' : form}, context_instance=RequestContext(request))

def deletewinnerpoints(request, id):    
    u = WinnerPoints.objects.get(pk=id).delete()
    values = WinnerPoints.objects.all()
    return render_to_response("winnerpointslist.html", {'values': values})
