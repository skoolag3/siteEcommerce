from django.shortcuts import render
from django.shortcuts import get_object_or_404, HttpResponseRedirect, render
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
            return HttpResponseRedirect(reverse('list_carrinho'))
    else:
        form = CarrinhoForm()
    return render(request, 'carrinho/carrinho_ins.html', {'form': form})


def list_carrinho(request):
    carrinhos = Carrinho.objects.all()
    return render(request, 'carrinho/carrinhos.html', {'objects': carrinhos})




def upd_carrinho(request, pk):
    obj = get_object_or_404(Carrinho, pk=pk)
    if request.method == 'POST':
        form = CarrinhoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            aviso = 'carrinho atualizado'
            messages.success(request, aviso)
            return HttpResponseRedirect(reverse('list_carrinho'))
    else:
        form = CarrinhoForm(instance=obj)
        context = {'form': form, 'obj': obj}
    return render(request, 'carrinho/carrinho_upd.html', context)


def del_carrinho(request, pk):
    obj = get_object_or_404(Carrinho, pk=pk)
    if request.method == 'POST':
        obj.delete()
        aviso = 'carrinho deletado'
        messages.success(request, aviso)
        return HttpResponseRedirect(reverse('list_carrinho'))
    context =  {'obj': obj}
    return render(request, 'carrinho/carrinho_del.html', context)

#crud carrinhoItem
def ins_carrinhoitem(request):
    if request.method == 'POST':
        form = CarrinhoItemForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = 'item carrinho inserido'
            messages.success(request, aviso)
            return HttpResponseRedirect(reverse('list_carrinhoitem'))
    else:
        form = CarrinhoItemForm()
    return render(request, 'carrinhoitem/carrinhoitem_ins.html', {'form': form})


def list_carrinhoitem(request):
    itens = CarrinhoItem.objects.all()
    return render(request, 'carrinhoitem/carrinhositem.html', {'objects': itens})

def upd_carrinhoitem(request, pk):
    obj = get_object_or_404(CarrinhoItem, pk=pk)
    if request.method == 'POST':
        form = CarrinhoItemForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            aviso = 'item carrinho atualizado'
            messages.success(request, aviso)
            return HttpResponseRedirect(reverse('list_carrinhoitem'))
    else:
        form = CarrinhoItemForm(instance=obj)
        context =  {'form': form, 'obj': obj}
    return render(request, 'carrinhoitem/carrinhoitem_upd.html', context)

def del_carrinhoitem(request, pk):
    obj = get_object_or_404(CarrinhoItem, pk=pk)
    if request.method == 'POST':
        obj.delete()
        aviso = 'item carrinho removido'
        messages.success(request, aviso)
        return HttpResponseRedirect(reverse('list_carrinhoitem'))
    context = {'obj': obj}
    return render(request, 'carrinhoitem/carrinhoitem_del.html', context)