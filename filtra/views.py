from django.shortcuts import render
from inserisci.models import Citazione
from django.shortcuts import redirect
from . import utils as u

def filtra(request):

    libri, autori, distinct_tags = u.var_menu_tendina()
    context = {
        'libri' : libri,
        'autori' : autori,
        'tags' : distinct_tags
    }

    return render(request, 'filtra.html', context)

def filtra_citazioni(request):

    libri, autori, tags = u.valori_filtro(request)
    citazioni = Citazione.objects.all()
    citazioni = u.applica_filtri(citazioni, libri, autori, tags)     
    libri_unici, autori_unici, distinct_tags = u.var_menu_tendina()
    context = {
        'citazioni': citazioni,
        'libri': libri_unici,
        'autori': autori_unici,
        'tags': distinct_tags,
        'request' : request,
        'libri_selezionati': libri,
        'autori_selezionati': autori,
        'tags_selezionati': tags,
    }

    return render(request, 'filtra.html', context)


def cancella_citazioni(request):
    if request.method == 'POST':
        # Recupera gli ID delle citazioni selezionate
        citazioni_selezionate = request.POST.getlist('citazioni_selezionate')
        if citazioni_selezionate:
            # Cancella le citazioni dal database
            Citazione.objects.filter(id__in=citazioni_selezionate).delete()
        libri, autori, distinct_tags = u.var_menu_tendina()
        libro, autore, tags = u.valori_filtro(request)
        citazioni = Citazione.objects.all()
        citazioni = u.applica_filtri(citazioni, libro, autore, tags)
        context = {
            'citazioni': citazioni,
            'libri_selezionati': libro,
            'autori_selezionati': autore,
            'tags_selezionati': tags,
            'libri' : libri,
            'autori' : autori,
            'tags' : distinct_tags
        }
        print(request.POST)
        return render(request, 'filtra.html', context)
    return redirect('filtra')


