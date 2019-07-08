from django.db import models


class Cliente(models.Model):
    
    nome = models.CharField(max_length=50)
    empresa = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=14)
    responsavel = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    solucao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome