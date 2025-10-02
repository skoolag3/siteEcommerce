from django.shortcuts import render

from apps.produtos.models import Produtos

def index(request):

    produtosRecentes = Produtos.objects.order_by('-dataCriado')[:8]

    produtosAlfabetico = Produtos.objects.order_by('nome')[:8]

    contexto = {
        'produtosRecentes': produtosRecentes,
        'produtosAlfabetico': produtosAlfabetico,
    }

    return render(request, 'home/index.html', contexto)
