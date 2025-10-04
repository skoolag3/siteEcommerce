from django.db import models
from django.conf import settings


class Empresa(models.Model):
    nome_fantasia = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=18, unique=True)
    data_fundacao = models.DateField(null=True, blank=True)
    endereco = models.CharField(max_length=200, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    cep = models.CharField(max_length=10, blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    site = models.URLField(blank=True)
    responsavel_legal = models.CharField(max_length=100, blank=True)  
    STATUS_CHOICES = [
        ('ativo'),
        ('inativo'),
        ('suspenso'),
        ('excluido'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nome_fantasia


class Vendedor(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vendedor')
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, blank=True, related_name='vendedores')
    STATUS_CHOICES = [
        ('ativo'),
        ('inativo'),
        ('suspenso'),
        ('excluido'),
        ('pendente_aprovacao'),
    ]
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pendente_aprovacao')
    comissao_percentual = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Vendedores"

    def __str__(self):
        return self.usuario.nome