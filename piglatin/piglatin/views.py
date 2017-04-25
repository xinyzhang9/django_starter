from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	return render(request,'home.html')


def translate(request):

	return HttpResponse('you are in translate page' + request.GET['originaltext'])