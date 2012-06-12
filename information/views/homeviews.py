#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response

def index(request):
  print 'ok'
  #return HttpResponse(u"Ol Mundo!")
  return render_to_response("home.html", {})
