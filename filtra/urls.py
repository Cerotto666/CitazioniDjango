from django.urls import path
from . import views

urlpatterns = [
    path('', views.filtra, name="filtra"),
    path("filtra_citazioni", views.filtra_citazioni, name = 'filtra_citazioni'),
    path("cancella_citazioni", views.cancella_citazioni, name="cancella_citazioni"),
]