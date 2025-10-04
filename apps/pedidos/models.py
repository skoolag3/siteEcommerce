from django.db import models
from django.conf import settings

class Pedido(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pedidos')
    endereco_entrega = models.ForeignKey('accounts.Endereco', on_delete=models.SET_NULL, null=True)
    
    STATUS_CHOICES = [
        ('pendente'),
        ('confirmado'),
        ('processando'),
        ('enviado'),
        ('entregue'),
        ('cancelado'),
        ('devolvido'),
        ('reembolsado'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    frete = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    codigo_rastreio = models.CharField(max_length=100, blank=True)
    observacoes = models.TextField(blank=True)

    class Meta:
        ordering = ['-data_criacao']

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.nome}"


class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey('products.Produto', on_delete=models.CASCADE)
    variacao = models.ForeignKey('products.ProdutoVariacao', on_delete=models.SET_NULL, null=True, blank=True)
    vendedor = models.ForeignKey('vendors.Vendedor', on_delete=models.SET_NULL, null=True)
    quantidade = models.PositiveIntegerField(null=False, default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    
    STATUS_CHOICES = [
        ('pendente'),
        ('confirmado'),
        ('enviado'),
        ('entregue'),
        ('cancelado'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        if self.variacao:
            return f"{self.quantidade} x {self.produto.nome} ({self.variacao})"
        return f"{self.quantidade} x {self.produto.nome}"