from django import forms

from apps.carrinho.models import Carrinho, CarrinhoItem


class CarrinhoForm(forms.ModelForm):
    class Meta:
        model = Carrinho
        fields = '__all__'
        widgets = {
            'criado_em': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'atualizado_em': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class CarrinhoItemForm(forms.ModelForm):
    class Meta:
        model = CarrinhoItem
        fields = '__all__'
        widgets = {
            'adicionado_em': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }