from django.db import models




class Pagamento(models.Model):
    pedido = models.OneToOneField('orders.Pedido', on_delete=models.CASCADE, related_name='pagamento')
    
    METODO_CHOICES = [
        ('pix'),
        ('credito'),
        ('debito'),
        ('boleto'),
    ]
    metodo = models.CharField(max_length=50, choices=METODO_CHOICES)
    
    STATUS_CHOICES = [
        ('pendente'),
        ('processando'),
        ('aprovado'),
        ('recusado'),
        ('cancelado'),
        ('estornado'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_pagamento = models.DateTimeField(null=True, blank=True)
    transacao_id = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"Pagamento #{self.id} - Pedido #{self.pedido.id}"