from django.db import models

# Create your models here.
class Pagamento(models.Model):
    pedido = models.OneToOneField('pedidos.Pedido', on_delete=models.CASCADE, related_name='pagamento')
    
    METODO_CHOICES = [
        ('pix', 'Pix'),
        ('credito', 'Credito'),
        ('debito', 'Debito'),
        ('boleto', 'Boleto'),
    ]
    metodo = models.CharField(max_length=50, choices=METODO_CHOICES)
    
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('processando', 'Processando'),
        ('aprovado', 'Aprovado'),
        ('recusado', 'Recusado'),
        ('cancelado', 'Cancelado'),
        ('estornado', 'Estornado'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_pagamento = models.DateTimeField(null=True, blank=True)
    transacao_id = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"Pagamento #{self.id} - Pedido #{self.pedido.id}"