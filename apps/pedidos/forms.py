from django import forms
from apps.pedidos.models import Pedido, PedidoItem


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        widgets = {
            'data_criacao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'data_atualizacao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class PedidoItemForm(forms.ModelForm):
    class Meta:
        model = PedidoItem
        fields = '__all__'