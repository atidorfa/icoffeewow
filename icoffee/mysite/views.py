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
        return render(request, 'gold.html')

def gold(request):
        return render(request, 'gold.html')

def offer(request):
        return render(request, 'offer.html')

def leveling(request):
        return render(request, '404.html')

def characters(request):
        return render(request, 'characters.html')

def summary(request):
        return render(request, 'summary.html')

def buy(request):
        return render(request, 'buy.html')

def sell(request):
        return render(request, 'sell.html')

def contact(request):
        return render(request, 'contact.html')

def mercadopago(request):
        return render(request, 'mercadopago.html')
