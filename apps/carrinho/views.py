from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrinho, ItemCarrinho
from .forms import ItemCarrinhoForm

def carrinhoView(request, identificador):
    carrinho = get_object_or_404(Carrinho, identificador=identificador)
    itens = ItemCarrinho.objects.filter(idCarrinho=identificador)

    if request.method == "POST":
        nova_forma = request.POST.get("formaPagamento")
        if nova_forma:
            carrinho.forma_pagamento = nova_forma
            carrinho.save()

    total = sum([i.subtotal() for i in itens])
    return render(request, "carrinho/carrinho.html", {
        "carrinho": carrinho,
        "itens": itens,
        "total": total
    })


def removerItem(request, item_id, identificador):
    item = get_object_or_404(ItemCarrinho, id=item_id, idCarrinho=identificador)
    item.delete()
    return redirect("carrinhoView", identificador=identificador)


def adicionarItem(request, identificador):
    if request.method == "POST":
        form = ItemCarrinhoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("carrinhoView", identificador=identificador)
    else:
        form = ItemCarrinhoForm(initial={"idCarrinho": identificador})
    return render(request, "carrinho/form_item.html", {"form": form, "identificador": identificador})
