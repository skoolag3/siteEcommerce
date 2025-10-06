from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('carrinho/', views.list_carrinho, name='list_carrinho'),
    path('carrinho/inserir/', views.ins_carrinho, name='ins_carrinho'),
    path('carrinho/atualizar/<int:pk>', views.upd_carrinho, name='upd_carrinho'),
    path('carrinho/deletar/<int:pk>', views.del_carrinho, name='del_carrinho'),

    path('carrinhoitem/', views.list_carrinhoitem, name='list_carrinhoitem'),
    path('carrinhoitem/inserir/', views.ins_carrinhoitem, name='ins_carrinhoitem'),
    path('carrinhoitem/atualizar/<int:pk>', views.upd_carrinhoitem, name='upd_carrinhoitem'),
    path('carrinhoitem/deletar/<int:pk>', views.del_carrinhoitem, name='del_carrinhoitem'),
]
    