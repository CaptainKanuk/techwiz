from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
#from pages.forms import RegisterForm
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.contrib import auth
from django.http import Http404


# Create your views here.

def index(request):
	context=RequestContext(request)
	return render_to_response('pages/index.html', context)

def notfound(request):
	context=RequestContext(request)
	return render_to_response('pages/404.html', context)


