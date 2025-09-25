from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from .forms import CadastroForm
from django.contrib import messages


def login(request):
    return render(request, 'usuarios/login.html')

def cadastro(request):
    form = CadastroForm()
    if form.is_valid():
        aviso = "Logue para entrar"
        messages.success(request, aviso)
        return redirect(reverse('login'))
    else:
        aviso = "Ocorreu um erro no cadastro"
        messages.error(request, aviso)
    return render(request, 'usuarios/cadastro.html', {'form': form})
