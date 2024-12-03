from django.shortcuts import render
from inserisci.models import Citazione

def citazioni(request, tipo, valore):

    if tipo == 'libro':
        citazioni = Citazione.objects.filter(nome_libro=valore).values_list('testo_citazione', flat=True)
        titolo = f"Citazioni dal libro: {valore}"
    elif tipo == 'autore':
        citazioni = Citazione.objects.filter(nome_autore=valore).values_list('testo_citazione', flat=True)
        titolo = f"Citazioni dell'autore: {valore}"
    else:
        citazioni = []
        titolo = "Tipo non valido"

    context = {
        'titolo': titolo,
        'citazioni': citazioni,
    }
    return render(request, 'citazioni.html', context)
