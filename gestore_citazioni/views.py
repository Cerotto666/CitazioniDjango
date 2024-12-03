from django.shortcuts import render
from inserisci.models import Citazione

def home_libri(request):
    libri = Citazione.objects.values_list('nome_libro', flat=True).distinct()
    context = {
        'libri': libri
    }
    return render(request, 'home_libri.html', context)

def home_autori(request):
    autori = Citazione.objects.values_list('nome_autore', flat=True).distinct()
    context = {
        'autori':autori
    }
    return render(request, 'home_autori.html',context)







