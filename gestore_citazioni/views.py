from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def citazioni_per_libro(request, libro):
    context = {
        'message': f"Citazioni per il libro {libro}"
    }
    return render(request, 'placeholder.html', context)

def citazioni_per_autore(request):
    context = {
        
    }
    return render(request, 'archivioAutori.html', context)

def aggiungi_citazione(request):
    context = {
        'message': "Pagina per aggiungere una citazione"
    }
    return render(request, 'placeholder.html', context)

