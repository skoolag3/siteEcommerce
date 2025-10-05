from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('excluido', 'Excluído'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo')

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class Subcategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='subcategorias')
    nome = models.CharField(max_length=200)
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('excluido', 'Excluído'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo')

    class Meta:
        verbose_name_plural = "Subcategorias"

    def __str__(self):
        return f"{self.categoria.nome} > {self.nome}"


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco_base = models.DecimalField(max_digits=10, decimal_places=2)
    vendedor = models.ForeignKey('vendedores.Vendedor', on_delete=models.CASCADE, related_name='produtos')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='produtos')
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='produtos')
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    peso = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True, help_text="Peso em KG")
    
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('excluido', 'Excluído'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.nome


class ProdutoVariacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='variacoes')
    sku = models.CharField(max_length=100, unique=True)
    tamanho = models.CharField(max_length=20, blank=True)
    cor = models.CharField(max_length=50, blank=True)
    #outros_atributos json
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    imagem = models.ImageField(upload_to='variacoes/', null=True, blank=True)
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('excluido', 'Excluído'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo')

    class Meta:
        verbose_name_plural = "Variações de Produto"

    def __str__(self):
        attrs = []
        if self.tamanho:
            attrs.append(self.tamanho)
        if self.cor:
            attrs.append(self.cor)
        return f"{self.produto.nome} - {' / '.join(attrs)} ({self.sku})"