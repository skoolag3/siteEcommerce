from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.listarProdutos, name='listarProdutos'),
    path('novo', views.criarProdutos, name='criarProdutos'),
    path('editar/<int:pk>', views.atualizarProdutos, name='atualizarProdutos'),
    path('deletar/<int:pk>', views.deletarProdutos, name='deletarProdutos'),
]
