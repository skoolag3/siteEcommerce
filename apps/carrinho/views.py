from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import reverse
from apps.carrinho.models import Carrinho, CarrinhoItem
from apps.carrinho.forms import CarrinhoForm, CarrinhoItemForm


#Create your views here.
def ins_carrinho(request):
    if request.method == 'POST':
        form = CarrinhoForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = 'carrinho criado'
            messages.success(request, aviso)
            return redirect(reverse('list_carrinho'))
    else:
        form = CarrinhoForm()
    return render(request, 'carrinho/form.html', {'form': form})


def list_carrinho(request):
    carrinhos = Carrinho.objects.all()
    return render(request, 'carrinho/list.html', {'objects': carrinhos})




def upd_carrinho(request, pk):
    obj = get_object_or_404(Carrinho, pk=pk)
    if request.method == 'POST':
        form = CarrinhoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            aviso = 'carrinho atualizado'
            messages.success(request, aviso)
            return redirect(reverse('list_carrinho'))
    else:
        form = CarrinhoForm(instance=obj)
    return render(request, 'carrinho/form.html', {'form': form})


def del_carrinho(request, pk):
    obj = get_object_or_404(Carrinho, pk=pk)
    if request.method == 'POST':
        obj.delete()
        aviso = 'carrinho deletado'
        messages.success(request, aviso)
        return redirect(reverse('list_carrinho'))
    return render(request, 'carrinho/delete.html', {'object': obj})

#crud carrinhoItem
def ins_carrinhoitem(request):
    if request.method == 'POST':
        form = CarrinhoItemForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = 'item carrinho inserido'
            messages.success(request, aviso)
            return redirect(reverse('list_carrinhoitem'))
    else:
        form = CarrinhoItemForm()
    return render(request, 'carrinhoitem/form.html', {'form': form})


def list_carrinhoitem(request):
    itens = CarrinhoItem.objects.all()
    return render(request, 'carrinhoitem/list.html', {'objects': itens})

def upd_carrinhoitem(request, pk):
    obj = get_object_or_404(CarrinhoItem, pk=pk)
    if request.method == 'POST':
        form = CarrinhoItemForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            aviso = 'item carrinho atualizado'
            messages.success(request, aviso)
            return redirect(reverse('list_carrinhoitem'))
    else:
        form = CarrinhoItemForm(instance=obj)
    return render(request, 'carrinhoitem/form.html', {'form': form})

def del_carrinhoitem(request, pk):
    obj = get_object_or_404(CarrinhoItem, pk=pk)
    if request.method == 'POST':
        obj.delete()
        aviso = 'item carrinho removido'
        messages.success(request, aviso)
        return redirect(reverse('list_carrinhoitem'))
    return render(request, 'carrinhoitem/delete.html', {'object': obj})