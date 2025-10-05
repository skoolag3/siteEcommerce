from django import forms
from apps.vendedores.models import Empresa, Vendedor


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        widgets = {
            'data_fundacao': forms.DateInput(attrs={'type': 'date'}),
            'data_criacao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'data_atualizacao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = '__all__'
        widgets = {
            'data_cadastro': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }