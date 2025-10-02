from django.shortcuts import render, redirect, get_object_or_404
from .models import Produtos
from .forms import ProdutosForm
from django.contrib import messages

def listarProdutos(request):
    produtos = Produtos.objects.all()
    return render(request, 'produtos/produtos.html', {'produtos': produtos})

def criarProdutos(request):
    if request.method == 'POST':
        form = ProdutosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto criado com sucesso!")
            return redirect('produtos:listarProdutos')
    else:
        form = ProdutosForm()
    return render(request, 'produtos/prod_create.html', {'form': form})

def atualizarProdutos(request, pk):
    produto = get_object_or_404(Produtos, pk=pk)
    if request.method == 'POST':
        form = ProdutosForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto atualizado com sucesso!")
            return redirect('produtos:listarProdutos')
    else:
        form = ProdutosForm(instance=produto)
    return render(request, 'produtos/prod_alt.html', {'form': form})

def deletarProdutos(request, pk):
    produto = get_object_or_404(Produtos, pk=pk)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, "Produto deletado com sucesso!")
        return redirect('produtos:listarProdutos')
    return render(request, 'produtos/prod_del.html', {'produto': produto})
