from django.db import models

class Citazione(models.Model):
    nome_libro = models.CharField(max_length=200)
    testo_citazone = models.TextField()
    nome_autore = models.CharField(max_length=100)
    tags = models.JSONField(default=list, blank=True)
    photo = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.nome_libro
