import datetime
from django.db import models
from django.utils import timezone

class Pergunta(models.Model):
    texto_pergunta = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField("date published")
    
    def __str__(self):
        return self.texto_pergunta

    def foi_publicado_recentemente(self):
        return self.data_publicacao >= timezone.now() - datetime.timedelta(days=1)


class Escolha(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto_escolha = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto_escolha