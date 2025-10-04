# apps/usuarios/forms.py
from django import forms

class CadastroForm(forms.Form):
    usuario = forms.CharField(
        label='Nome de Usuário',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Digite seu usuário'
        })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Digite seu email'
        })
    )
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Digite sua senha'
        })
    )
    senhaconfirm = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Confirme sua senha'
        })
    )


class LoginForm(forms.Form):
    usuario = forms.CharField(
        label='Usuário',
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu usuário',
            'size': 30
        })
    )
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha',
            'size': 30
        })
    )