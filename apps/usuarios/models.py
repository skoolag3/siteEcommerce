from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.nome or self.username


class Endereco(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enderecos')
    nome_destinatario = models.CharField(max_length=150)
    cep = models.CharField(max_length=10)
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    telefone_contato = models.CharField(max_length=20)
    principal = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Endereços"

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.cidade}/{self.estado}"