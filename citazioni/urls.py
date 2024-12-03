from django.urls import path
from . import views

urlpatterns = [
    path('<str:tipo>/<str:valore>/', views.citazioni, name="citazioni"),
]
