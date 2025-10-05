from django import forms
from apps.usuarios.models import Endereco, User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'nome', 'email', 'telefone', 'cpf', 'data_nascimento']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'
        widgets = {
            'criado_em': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }