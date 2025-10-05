from django.shortcuts import get_object_or_404, redirect, render
from apps.produtos.models import Categoria, Produto, ProdutoVariacao, Subcategoria
from apps.produtos.forms import CategoriaForm, ProdutoForm, ProdutoVariacaoForm, SubcategoriaForm
from django.contrib import messages
from django.urls import reverse


# Create your views here.

def ins_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = 'categoria criada'
            messages.success(request, aviso)
            return redirect(reverse('list_categoria'))
    else:
        form = CategoriaForm()
    return render(request, 'categoria/form.html', {'form': form})


def list_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria/list.html', {'objects': categorias})



def upd_categoria(request, pk):
    obj = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            aviso = 'categoria atualizada'
            messages.success(request, aviso)
            return redirect(reverse('list_categoria'))
    else:
        form = CategoriaForm(instance=obj)
    return render(request, 'categoria/form.html', {'form': form})


def del_categoria(request, pk):
    obj = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        obj.delete()
        aviso = 'categoria deletada'
        messages.success(request, aviso)
        return redirect(reverse('list_categoria'))
    return render(request, 'categoria/delete.html', {'object': obj})

#crud subcategoria
def ins_subcategoria(request):
    if request.method == 'POST':
        form = SubcategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = 'subcategoria inserida'
            messages.success(request, aviso)
            return redirect(reverse('list_subcategoria'))
    else:
        form = SubcategoriaForm()
    return render(request, 'subcategoria/form.html', {'form': form})

def list_subcategoria(request):
    subcategorias = Subcategoria.objects.all()
    return render(request, 'subcategoria/list.html', {'objects': subcategorias})

def upd_subcategoria(request, pk):
    obj = get_object_or_404(Subcategoria, pk=pk)
    if request.method == 'POST':
        form = SubcategoriaForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            aviso = 'subcategoria atualizada'
            messages.success(request, aviso)
            return redirect(reverse('list_subcategoria'))
    else:
        form = SubcategoriaForm(instance=obj)
    return render(request, 'subcategoria/form.html', {'form': form})

def del_subcategoria(request, pk):
    obj = get_object_or_404(Subcategoria, pk=pk)
    if request.method == 'POST':
        obj.delete()
        aviso = 'subcategoria deletada'
        messages.success(request, aviso)
        return redirect(reverse('list_subcategoria'))
    return render(request, 'subcategoria/delete.html', {'object': obj})

#crud produto
def ins_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            aviso = 'produto inserido'
            messages.success(request, aviso)
            return redirect(reverse('list_produto'))
    else:
        form = ProdutoForm()
    return render(request, 'produto/form.html', {'form': form})


def list_produto(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/list.html', {'objects': produtos})

def upd_produto(request, pk):
    obj = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            aviso = 'produto atualizado'
            messages.success(request, aviso)
            return redirect(reverse('list_produto'))
    else:
        form = ProdutoForm(instance=obj)
    return render(request, 'produto/form.html', {'form': form})


def del_produto(request, pk):
    obj = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        obj.delete()
        aviso = 'produto deletado'
        messages.success(request, aviso)
        return redirect(reverse('list_produto'))
    return render(request, 'produto/delete.html', {'object': obj})


#crud produtovariacao

def ins_produtovariacao(request):
    if request.method == 'POST':
        form = ProdutoVariacaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            aviso = 'variacao inserida'
            messages.success(request, aviso)
            return redirect(reverse('list_produtovariacao'))
    else:
        form = ProdutoVariacaoForm()
    return render(request, 'produtovariacao/form.html', {'form': form})


def list_produtovariacao(request):
    variacoes = ProdutoVariacao.objects.all()
    return render(request, 'produtovariacao/list.html', {'objects': variacoes})



def upd_produtovariacao(request, pk):
    obj = get_object_or_404(ProdutoVariacao, pk=pk)
    if request.method == 'POST':
        form = ProdutoVariacaoForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            aviso = 'variacao atualizado'
            messages.success(request, aviso)
            return redirect(reverse('list_produtovariacao'))
    else:
        form = ProdutoVariacaoForm(instance=obj)
    return render(request, 'produtovariacao/form.html', {'form': form})

def del_produtovariacao(request, pk):
    obj = get_object_or_404(ProdutoVariacao, pk=pk)
    if request.method == 'POST':
        obj.delete()
        aviso = 'variacao deletada'
        messages.success(request, aviso)
        return redirect(reverse('list_produtovariacao'))
    return render(request, 'produtovariacao/delete.html', {'object': obj})