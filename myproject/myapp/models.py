from django.db import models


class EPIgenerico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    prazo_dias = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Colaborador(models.Model):
    nome = models.CharField(max_length=100) 
    cpf = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    nome = models.CharField(max_length=100)
    condicoes = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    data_prevista = models.DateField(null=True)
    data_devolucao = models.DateField(null=True)
    data_emprestimo = models.DateField(null=True)
    id_EPIgenerico_fk = models.ForeignKey(EPIgenerico, on_delete=models.CASCADE)
    motivo_devolucao = models.TextField()

    def __str__(self):
        return self.nome

class Colaborador(models.Model):
    nome = models.CharField(max_length=100) 
    cpf = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

