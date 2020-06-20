from django.shortcuts import render
from . import getdata

def index(request): 
	states_data = states_report()


	context = dict(**states_data)
	return render(request, template_name='index.html', context=context)

def guidelines(request):
	return render(request, template_name='guidelines.html')

def about(request):
	return render(request, template_name='about.html')

def states_report():
	df = getdata.states_report()
	return {'states_data': df}
