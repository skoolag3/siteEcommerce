from django.urls import path
from . import views

app_name = 'carrinho'

urlpatterns = [
    path('<str:identificador>', views.carrinhoView, name='carrinhoView'),
    path('remover/<int:item_id>/<str:identificador>/', views.removerItem, name='removerItem'),
    path('adicionar/<str:identificador>/', views.adicionarItem, name='adicionarItem'),
]
