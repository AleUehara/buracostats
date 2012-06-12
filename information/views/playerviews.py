#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from forms import FormPlayer
from django.template import RequestContext

def player(request):
	return render_to_response("list.html", {})

def addplayer(request):
	form = FormPlayer(request.POST, request.FILES)
	if request.method == 'POST':
		form = FormPlayer(request.POST, request.FILES)
		#if form.is_valid():
		#	dados = form.cleaned_data
		#	send_post = 'envia_teste.py'
		#	has_error = os.system('python ../../%s' %(send_post))
		#	if has_error:
		#		return render_to_response('adiciona.html', {'error' : 'ERRO ao enviar dados','form' : form,})
		#	print 'enviado'
		#	return render_to_response("salvo.html", {})

	else:
		#year = str(datetime.now().year)
		#form = FormPost({'date': year, })
		pass
	return render_to_response("add.html", {'form' : form}, context_instance=RequestContext(request))