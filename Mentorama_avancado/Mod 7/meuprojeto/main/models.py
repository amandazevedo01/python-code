from django.db import models
from datetime import datetime as dt

# Create your models here.

class ProjetoDjango(models.Model):
    # Aqui definimos as colunas que teremos em nosso banco de dados
    titulo = models.CharField(max_length=50) #CharField(max_lenght=50) caracter, com no maximo 50 carac
    descricao = models.TextField() # texto
    ano = models.CharField(max_length=4)
    data = models.DateTimeField("Publicado em",default=dt.now())

    def __str__(self):
        return self.titulo