from django import forms
from apps.produtos.models import Categoria, Produto, ProdutoVariacao, Subcategoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class SubcategoriaForm(forms.ModelForm):
    class Meta:
        model = Subcategoria
        fields = '__all__'

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'criado_em': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'atualizado_em': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ProdutoVariacaoForm(forms.ModelForm):
    class Meta:
        model = ProdutoVariacao
        fields = '__all__'