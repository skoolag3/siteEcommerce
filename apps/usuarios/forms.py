# apps/usuarios/forms.py
from django import forms

class CadastroForm(forms.Form):
    usuario = forms.CharField(
        label='Nome de Usuário',
        max_length=150,
        help_text='Digite seu nome de usuário',
        widget=forms.TextInput(attrs={'type':'text', 'size':30})
    )
    email = forms.EmailField(
        label='Email',
        help_text='Digite seu email',
        widget=forms.EmailInput(attrs={'type':'email', 'size':30})
    )
    senha = forms.CharField(
        label='Senha',
        help_text='Digite sua senha',
        widget=forms.PasswordInput(attrs={'type':'password', 'size':30})
    )
    senhaconfirm = forms.CharField(
        label='Confirmar Senha',
        help_text='Digite sua senha novamente',
        widget=forms.PasswordInput(attrs={'type':'password', 'size':30})
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