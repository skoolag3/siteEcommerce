from django.http import HttpResponseRedirect
from apps.usuarios.forms import EnderecoForm, UserForm
from apps.usuarios.models import Endereco, User
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = request.POST.get('password')
            user.set_password(password)
            user.save()
            aviso = 'Cadastro realizado com sucesso!'
            messages.success(request, aviso)
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserForm()
    return render(request, 'auth/cadastro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            aviso = f'Bem-vindo, {user.nome}!'
            messages.success(request, aviso)
            next_url = request.GET.get('next', reverse('list_user'))
            return redirect(next_url)
        else:
            aviso = 'Usuário ou senha inválidos!'
            messages.error(request, aviso)
    return render(request, 'auth/login.html')

def user_logout(request):
    logout(request)
    aviso = 'logout concluido'
    messages.success(request, aviso)
    return redirect(reverse('user_login'))




def ins_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = 'Inserido com sucesso!'
            messages.success(request, aviso)
            return redirect(reverse('list_user'))
    else:
        form = UserForm()
    return render(request, 'user/form.html', {'form': form})


def list_user(request):
    users = User.objects.all()
    return render(request, 'user/list.html', {'objects': users})



def upd_user(request, pk):
    obj = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            aviso = 'Atualizado com sucesso!'
            messages.success(request, aviso)
            return redirect(reverse('list_user'))
    else:
        form = UserForm(instance=obj)
    return render(request, 'user/form.html', {'form': form})


def del_user(request, pk):
    obj = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        obj.delete()
        aviso = 'Deletado com sucesso!'
        messages.success(request, aviso)
        return redirect(reverse('list_user'))
    return render(request, 'user/delete.html', {'object': obj})


# crud endereço 


def ins_endereco(request):
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = 'Criado com sucesso!'
            messages.success(request, aviso)
            return redirect(reverse('list_endereco'))
    else:
        form = EnderecoForm()
    return render(request, 'endereco/form.html', {'form': form})


def list_endereco(request):
    enderecos = Endereco.objects.all()
    return render(request, 'endereco/list.html', {'objects': enderecos})



def upd_endereco(request, pk):
    obj = get_object_or_404(Endereco, pk=pk)
    if request.method == 'POST':
        form = EnderecoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            aviso = 'Atualizado com sucesso!'
            messages.success(request, aviso)
            return redirect(reverse('list_endereco'))
    else:
        form = EnderecoForm(instance=obj)
    return render(request, 'endereco/form.html', {'form': form})


def del_endereco(request, pk):
    obj = get_object_or_404(Endereco, pk=pk)
    if request.method == 'POST':
        obj.delete()
        aviso = 'Deletado com sucesso!'
        messages.success(request, aviso)
        return redirect(reverse('list_endereco'))
    return render(request, 'endereco/delete.html', {'object': obj})