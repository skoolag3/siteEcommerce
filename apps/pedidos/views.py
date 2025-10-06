from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.urls import reverse
from apps.pedidos.forms import PedidoForm, PedidoItemForm
from apps.pedidos.models import Pedido, PedidoItem

#Create your views here
def ins_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = "Pedido criado"
            messages.success(request, aviso)
            return HttpResponseRedirect(reverse('list_pedido'))
    else:
        form = PedidoForm()
    return render(request, 'pedido/pedido_ins.html', {'form': form})

def list_pedido(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedido/pedidos.html', {'objects': pedidos})

def upd_pedido(request, pk):
    obj = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            aviso = "Pedido atualizado"
            messages.success(request, aviso)
            return HttpResponseRedirect(reverse('list_pedido'))
    else:
        form = PedidoForm(instance=obj)
        context = {'form': form, 'obj': obj}
    return render(request, 'pedido/pedido_upd.html', context)

def del_pedido(request, pk):
    obj = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        obj.delete()
        aviso = "Pedido deletado"
        messages.success(request, aviso)
        return HttpResponseRedirect(reverse('list_pedido'))
    context = {'object': obj}
    return render(request, 'pedido/pedido_del.html', context)

# crud -pedidoItem
def ins_pedidoitem(request):
    if request.method == 'POST':
        form = PedidoItemForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = "Item do pedido inserido"
            messages.success(request, aviso)
            return HttpResponseRedirect(reverse('list_pedidoitem'))
    else:
        form = PedidoItemForm()
    return render(request, 'pedidoitem/pedidoitem_ins.html', {'form': form})

def list_pedidoitem(request):
    itens = PedidoItem.objects.all()
    return render(request, 'pedidoitem/pedidositem.html', {'objects': itens})

def upd_pedidoitem(request, pk):
    obj = get_object_or_404(PedidoItem, pk=pk)
    if request.method == 'POST':
        form = PedidoItemForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            aviso = "Item do pedido atualizado"
            messages.success(request, aviso)
            return HttpResponseRedirect(reverse('list_pedidoitem'))
    else:
        form = PedidoItemForm(instance=obj)
        context = {'form': form, 'obj': obj}
    return render(request, 'pedidoitem/pedidoitem_upd.html', context)

def del_pedidoitem(request, pk):
    obj = get_object_or_404(PedidoItem, pk=pk)
    if request.method == 'POST':
        obj.delete()
        aviso = "Item do pedido deletado"
        messages.success(request, aviso)
        return HttpResponseRedirect(reverse('list_pedidoitem'))
    context = {'object': obj}
    return render(request, 'pedidoitem/pedidoitem_del.html', context)
