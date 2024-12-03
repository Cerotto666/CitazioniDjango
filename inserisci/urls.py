from django.urls import path
from . import views

urlpatterns = [
    path('', views.aggiungi_citazione, name='aggiungi_citazione'),
    path('inserisci',views.inserisci_citazione, name='inserisci_citazione'),
]