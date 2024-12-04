from inserisci.models import Citazione

def var_menu_tendina():
    libri = Citazione.objects.values_list('nome_libro', flat=True).distinct()
    autori = Citazione.objects.values_list('nome_autore', flat=True).distinct()
    all_tags = Citazione.objects.values_list('tags', flat=True)
    distinct_tags = set(tag for tags in all_tags for tag in tags)

    return (libri, autori, distinct_tags)

def valori_filtro(request):
    # Recupera i parametri di filtro come liste
    if request.method == 'GET':
        libri = request.GET.getlist('libro')  # Recupera tutti i libri selezionati
        autori = request.GET.getlist('autore')  # Recupera tutti gli autori selezionati
        tags = request.GET.getlist('tags')  # Recupera tutti i tag selezionati
    else:
        libri = request.POST.getlist('libro')  # Recupera tutti i libri selezionati
        autori = request.POST.getlist('autore')  # Recupera tutti gli autori selezionati
        tags = request.POST.getlist('tags')  # Recupera tutti i tag selezionati

    return (libri, autori, tags)

def applica_filtri(citazioni, libri, autori, tags):
        # Applica i filtri
    if libri:
        citazioni = citazioni.filter(nome_libro__in=libri)  # Filtro per più libri
    if autori:
        citazioni = citazioni.filter(nome_autore__in=autori)  # Filtro per più autori
    if tags:
        filtered_citazioni = set()
        for tag in tags:
            filtered_citazioni.update(citazione for citazione in citazioni if tag in citazione.tags)
            citazioni = list(filtered_citazioni) 

    return citazioni


