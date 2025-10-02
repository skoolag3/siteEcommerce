from django.db import models

class Carrinho(models.Model):
    identificador = models.CharField(max_length=100, unique=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Carrinho {self.identificador}"


class ItemCarrinho(models.Model):
    nomeProduto = models.CharField(max_length=255)
    precoUni = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=1)
    idCarrinho = models.CharField(max_length=100)

    def subtotal(self):
        return self.precoUni * self.quantidade

    def __str__(self):
        return f"{self.nomeProduto} (x{self.quantidade})"
