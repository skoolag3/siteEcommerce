from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from apps.pedidos.forms import PedidoForm, PedidoItemForm
from apps.pedidos.models import Pedido, PedidoItem

# Create your views here.


def ins_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = 'pedido criado'
            messages.success(request, aviso)
            return redirect(reverse('list_pedido'))
    else:
        form = PedidoForm()
    return render(request, 'pedido/form.html', {'form': form})


def list_pedido(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedido/list.html', {'objects': pedidos})


def upd_pedido(request, pk):
    obj = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            aviso = 'pedido atualizado'
            messages.success(request, aviso)
            return redirect(reverse('list_pedido'))
    else:
        form = PedidoForm(instance=obj)
    return render(request, 'pedido/form.html', {'form': form})

def del_pedido(request, pk):
    obj = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        obj.delete()
        aviso = 'pedido deletado'
        messages.success(request, aviso)
        return redirect(reverse('list_pedido'))
    return render(request, 'pedido/delete.html', {'object': obj})

#crud pedidoItem

def ins_pedidoitem(request):
    if request.method == 'POST':
        form = PedidoItemForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = 'itenm do pedido inserido'
            messages.success(request, aviso)
            return redirect(reverse('list_pedidoitem'))
    else:
        form = PedidoItemForm()
    return render(request, 'pedidoitem/form.html', {'form': form})

def list_pedidoitem(request):
    itens = PedidoItem.objects.all()
    return render(request, 'pedidoitem/list.html', {'objects': itens})


def upd_pedidoitem(request, pk):
    obj = get_object_or_404(PedidoItem, pk=pk)
    if request.method == 'POST':
        form = PedidoItemForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            aviso = 'item do pedido atualizado'
            messages.success(request, aviso)
            return redirect(reverse('list_pedidoitem'))
    else:
        form = PedidoItemForm(instance=obj)
    return render(request, 'pedidoitem/form.html', {'form': form})

def del_pedidoitem(request, pk):
    obj = get_object_or_404(PedidoItem, pk=pk)
    if request.method == 'POST':
        obj.delete()
        aviso = 'item do pedido deletado'
        messages.success(request, aviso)
        return redirect(reverse('list_pedidoitem'))
    return render(request, 'pedidoitem/delete.html', {'object': obj})