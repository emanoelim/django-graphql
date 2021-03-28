from django.db import models


class UnidadeMedida(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Receita(models.Model):
    nome = models.CharField(max_length=250)

    def __str__(self):
        return self.nome


class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.DecimalField(max_digits=5, decimal_places=2)
    unidade_medida = models.ForeignKey(UnidadeMedida, null=True, on_delete=models.SET_NULL, related_name='unidade_ingrediente')
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE, related_name='receita_ingrediente')

    def __str__(self):
        return self.receita.__str__() + ' - ' + self.nome
