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




def citazioni_per_libro(request, libro):
    context = {
        'message': f"Citazioni per il libro {libro}"
    }
    return render(request, 'placeholder.html', context)

def citazioni_per_autore(request, autore):
    context = {
        'message': f"Citazioni per l'autore {autore}"
    }
    return render(request, 'placeholder.html', context)





def aggiungi_citazione(request):
    context = {
        'message': "Pagina per aggiungere una citazione"
    }
    return render(request, 'placeholder.html', context)

