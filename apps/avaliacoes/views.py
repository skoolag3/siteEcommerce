from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import reverse
from apps.avaliacoes.models import Avaliacao
from apps.avaliacoes.forms import AvaliacaoForm

# Create your views here.

def ins_avaliacao(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = 'avaliação inseridaa'
            messages.success(request, aviso)
            return HttpResponseRedirect(reverse('list_avaliacao'))
    else:
        form = AvaliacaoForm()
    return render(request, 'avaliacao/avaliacao_ins.html', {'form': form})


def list_avaliacao(request):
    avaliacoes = Avaliacao.objects.all()
    return render(request, 'avaliacao/avaliacoes.html', {'objects': avaliacoes})



def upd_avaliacao(request, pk):
    obj = get_object_or_404(Avaliacao, pk=pk)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            aviso = 'avaliação atualizada'
            messages.success(request, aviso)
            return HttpResponseRedirect(reverse('list_avaliacao'))
    else:
        form = AvaliacaoForm(instance=obj)
        context = {'form': form, 'obj': obj}
    return render(request, 'avaliacao/avaliacao_upd.html', context)


def del_avaliacao(request, pk):
    obj = get_object_or_404(Avaliacao, pk=pk)
    if request.method == 'POST':
        obj.delete()
        aviso = 'avaliação deletada'
        messages.success(request, aviso)
        return HttpResponseRedirect(reverse('list_avaliacao'))
    context = {'object': obj}
    return render(request, 'avaliacao/avaliacao_del.html', context)