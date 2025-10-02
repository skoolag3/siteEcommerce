from django import forms
from .models import Carrinho, ItemCarrinho

class CarrinhoForm(forms.ModelForm):
    class Meta:
        model = Carrinho
        fields = ['identificador']


class ItemCarrinhoForm(forms.ModelForm):
    class Meta:
        model = ItemCarrinho
        fields = ['nomeProduto', 'precoUni', 'quantidade', 'idCarrinho']
