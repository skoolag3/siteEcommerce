from django.shortcuts import render
from django.shortcuts import get_object_or_404, HttpResponseRedirect, render
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
            return HttpResponseRedirect(reverse('list_pagamento'))
    else:
        form = PagamentoForm()
    return render(request, 'pagamento/pagamento_ins.html', {'form': form})


def list_pagamento(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'pagamento/pagamentos.html', {'objects': pagamentos})



def upd_pagamento(request, pk):
    obj = get_object_or_404(Pagamento, pk=pk)
    if request.method == 'POST':
        form = PagamentoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            aviso = 'Pagamento atualizado'
            messages.success(request, aviso)
            return HttpResponseRedirect(reverse('list_pagamento'))
    else:
        form = PagamentoForm(instance=obj)
        context = {'form': form, 'obj': obj}
    return render(request, 'pagamento/pagamento_upd.html', context)


def del_pagamento(request, pk):
    obj = get_object_or_404(Pagamento, pk=pk)
    if request.method == 'POST':
        obj.delete()
        aviso = 'Pagamento deletado'
        messages.success(request, aviso)
        return HttpResponseRedirect(reverse('list_pagamento'))
    context = {'obj': obj}
    return render(request, 'pagamento/pagamento_del.html', context)