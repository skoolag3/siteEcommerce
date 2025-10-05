from django import forms
from apps.pagamento.models import Pagamento


class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = '__all__'
        widgets = {
            'data_criacao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'data_pagamento': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
