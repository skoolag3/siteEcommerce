from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import reverse
from apps.vendedores.models import Empresa, Vendedor
from apps.vendedores.forms import EmpresaForm, VendedorForm


# Create your views here.

def ins_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = 'empresa criada'
            messages.success(request, aviso)
            return HttpResponseRedirect(reverse('list_empresa'))
    else:
        form = EmpresaForm()
    return render(request, 'empresas/empresa_ins.html', {'form': form})


def list_empresa(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresas/empresas.html', {'objects': empresas})


def upd_empresa(request, pk):
    obj = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            aviso = 'empresa atualizada'
            messages.success(request, aviso)
            return HttpResponseRedirect(reverse('list_empresa'))
    else:
        form = EmpresaForm(instance=obj)
        context = {'form': form, 'obj': obj}
    return render(request, 'empresas/empresa_upd.html', context)

def del_empresa(request, pk):
    obj = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        obj.delete()
        aviso = 'empresa deletada'
        messages.success(request, aviso)
        return HttpResponseRedirect(reverse('list_empresa'))
    context = {'object': obj}
    return render(request, 'empresas/empresa_del.html', context)


#crud vendedor
def ins_vendedor(request):
    if request.method == 'POST':
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = 'vendedor inserido'
            messages.success(request, aviso)
            return HttpResponseRedirect(reverse('list_vendedor'))
    else:
        form = VendedorForm()
    return render(request, 'vendedor/vendedor_ins.html', {'form': form})


def list_vendedor(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'vendedor/vendedores.html', {'objects': vendedores})


def upd_vendedor(request, pk):
    obj = get_object_or_404(Vendedor, pk=pk)
    if request.method == 'POST':
        form = VendedorForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            aviso = 'vendedor atualizado'
            messages.success(request, aviso)
            return HttpResponseRedirect(reverse('list_vendedor'))
    else:
        form = VendedorForm(instance=obj)
        context = {'form': form, 'obj': obj}
    return render(request, 'vendedor/vendedor_upd.html', context)

def del_vendedor(request, pk):
    obj = get_object_or_404(Vendedor, pk=pk)
    if request.method == 'POST':
        obj.delete()
        aviso = 'vendedor deletado'
        messages.success(request, aviso)
        return HttpResponseRedirect(reverse('list_vendedor'))
    context = {'object': obj}
    return render(request, 'vendedor/vendedor_del.html', context)