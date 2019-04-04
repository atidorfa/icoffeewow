from django.shortcuts import render
from django.http import HttpResponse, Http404

def index(request):
    return render(request, 'index.html')

def instagram(request):
    return render(request, 'instagram.html')

def mercadolibre(request):
    return render(request, 'mercadolibre.html')

def facebook(request):
    return render(request, 'facebook.html')


