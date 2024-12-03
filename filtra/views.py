from django.shortcuts import render
from inserisci.models import Citazione
from django.shortcuts import redirect

def filtra(request):
    libri = Citazione.objects.values_list('nome_libro', flat=True).distinct()
    autori = Citazione.objects.values_list('nome_autore', flat=True).distinct()
    all_tags = Citazione.objects.values_list('tags', flat=True)
    distinct_tags = set(tag for tags in all_tags for tag in tags)
    context = {
        'libri' : libri,
        'autori' : autori,
        'tags' : distinct_tags
    }

    return render(request, 'filtra.html', context)

def filtra_citazioni(request):
    # Recupera i parametri di filtro come liste
    libri = request.GET.getlist('libro')  # Recupera tutti i libri selezionati
    autori = request.GET.getlist('autore')  # Recupera tutti gli autori selezionati
    tags = request.GET.getlist('tags')  # Recupera tutti i tag selezionati

    # Inizializza il queryset per le citazioni
    citazioni = Citazione.objects.all()

    # Applica i filtri
    if libri:
        citazioni = citazioni.filter(nome_libro__in=libri)  # Filtro per più libri
    if autori:
        citazioni = citazioni.filter(nome_autore__in=autori)  # Filtro per più autori
    if tags:
        for tag in tags:
            citazioni = [citazione for citazione in citazioni if tags in citazione.tags]  # Filtro per ogni tag
            
    # Recupera tutti i valori unici per popolare i menu a tendina
    libri_unici = Citazione.objects.values_list('nome_libro', flat=True).distinct()
    autori_unici = Citazione.objects.values_list('nome_autore', flat=True).distinct()
    all_tags = Citazione.objects.values_list('tags', flat=True)
    distinct_tags = set(tag for tags in all_tags for tag in tags)

    # Prepara il contesto per il template
    context = {
        'citazioni': citazioni,
        'libri': libri_unici,
        'autori': autori_unici,
        'tags': distinct_tags,
        'request' : request
    }

    return render(request, 'filtra.html', context)


def cancella_citazioni(request):
    if request.method == 'POST':
        # Recupera gli ID delle citazioni selezionate
        citazioni_selezionate = request.POST.getlist('citazioni_selezionate')

        if citazioni_selezionate:
            # Cancella le citazioni dal database
            Citazione.objects.filter(id__in=citazioni_selezionate).delete()

        # Recupera i filtri dal form
        libro = request.POST.getlist('libro', [])
        autore = request.POST.getlist('autore', [])
        tags = request.POST.getlist('tags', [])

        # Costruisce i parametri per il redirect
        query_params = []
        if libro:
            query_params.extend([f"libro={l}" for l in libro])
        if autore:
            query_params.extend([f"autore={a}" for a in autore])
        if tags:
            query_params.extend([f"tags={t}" for t in tags])
        
        query_string = "&".join(query_params)

        # Reindirizza alla pagina del filtro con i parametri
        return redirect(f"/filtra?{query_string}")

    # Se non è una richiesta POST, reindirizza o restituisci un errore
    return redirect('filtra')


