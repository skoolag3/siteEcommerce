from django.db import models

class Produtos(models.Model):
    idProdutos = models.AutoField(primary_key=True)  # chave primária customizada
    nome = models.CharField("Nome do Produto", max_length=200)
    preco = models.DecimalField("Preço do Produto", max_digits=10, decimal_places=2)
    estoque = models.IntegerField("Estoque do Produto")
    descricao = models.TextField("Descrição do Produto")
    imagem = models.TextField("Imagem do Produto")  # ideal seria usar ImageField
    categoria = models.CharField("Categoria do Produto", max_length=100)
    dataCriado = models.DateTimeField("Data de Criação do Produto", auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
