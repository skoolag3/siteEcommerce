from django.db import models
from django.conf import settings

class Carrinho(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='carrinhos')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    STATUS_CHOICES = [
        ('ativo'),
        ('finalizado'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo')

    def __str__(self):
        return f"Carrinho {self.id} - {self.usuario.nome}"


class CarrinhoItem(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey('products.Produto', on_delete=models.CASCADE)
    variacao = models.ForeignKey('products.ProdutoVariacao', on_delete=models.CASCADE, null=True, blank=True)
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    adicionado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['carrinho', 'produto', 'variacao'], name='idx_carrinho_item')
        ]

    def __str__(self):
        if self.variacao:
            return f"{self.quantidade} x {self.produto.nome} ({self.variacao})"
        return f"{self.quantidade} x {self.produto.nome}"