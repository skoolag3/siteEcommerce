from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import reverse
from apps.pagamento.models import Pagamento
from apps.pagamento.forms import PagamentoForm

# Create your views here.

def ins_pagamento(request):
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = 'Pagamento criado'
            messages.success(request, aviso)
            return redirect(reverse('list_pagamento'))
    else:
        form = PagamentoForm()
    return render(request, 'pagamento/form.html', {'form': form})


def list_pagamento(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'pagamento/list.html', {'objects': pagamentos})



def upd_pagamento(request, pk):
    obj = get_object_or_404(Pagamento, pk=pk)
    if request.method == 'POST':
        form = PagamentoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            aviso = 'Pagamento atualizado'
            messages.success(request, aviso)
            return redirect(reverse('list_pagamento'))
    else:
        form = PagamentoForm(instance=obj)
    return render(request, 'pagamento/form.html', {'form': form})


def del_pagamento(request, pk):
    obj = get_object_or_404(Pagamento, pk=pk)
    if request.method == 'POST':
        obj.delete()
        aviso = 'Pagamento deletado'
        messages.success(request, aviso)
        return redirect(reverse('list_pagamento'))
    return render(request, 'pagamento/delete.html', {'object': obj})