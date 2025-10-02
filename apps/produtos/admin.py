from django.contrib import admin
from .models import Produtos

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('idProdutos', 'nome', 'preco', 'estoque', 'categoria', 'dataCriado')
    list_filter = ('categoria', 'dataCriado')
    search_fields = ('nome', 'categoria')
