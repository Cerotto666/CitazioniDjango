from django.shortcuts import redirect, render
from inserisci.models import Citazione
from filtra import utils as u

def aggiungi_citazione(request):
    libri, autori, distinct_tags = u.var_menu_tendina()
    context = {
        'libri' : libri,
        'autori' : autori,
        'tags' : distinct_tags
    }
    return render(request, 'inserisci.html', context)

def inserisci_citazione(request):
        print("TUtto ok")
        libro = request.POST.get('libro')
        autore = request.POST.get('autore')
        citazione = request.POST.get('citazione')
        tags = request.POST.get('tags')

        # Converte i tags da stringa separata da virgola a lista
        tags_list = [tag.strip() for tag in tags.split(',')] if tags else []

        # Salva la citazione nel database
        Citazione.objects.create(
            nome_libro=libro,
            nome_autore=autore,
            testo_citazione=citazione,
            tags=tags_list
        )
        
        return redirect('home_libri')  
    #return render(request, 'inserisci_citazione.html')

