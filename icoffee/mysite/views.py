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

def pagamenos(request):
        return render(request, 'pagamenos.html')

def wow(request):
        return render(request, 'wow.html')

def wow_classic_gold(request):
        return render(request, 'wow-classic-gold.html')

def offer(request):
        return render(request, 'offer.html')
