from django.db import models
from django.conf import settings

# Create your models here.
class Avaliacao(models.Model):
    produto = models.ForeignKey('produtos.Produto', on_delete=models.CASCADE, related_name='avaliacoes')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='avaliacoes')
    pedido = models.ForeignKey('pedidos.Pedido', on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=2, decimal_places=1)
    comentario = models.TextField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['produto', 'usuario', 'pedido']
        ordering = ['-data_criacao']
    
    def __str__(self):
        return f"{self.usuario.nome} - {self.produto.nome} ({self.nota}★)"