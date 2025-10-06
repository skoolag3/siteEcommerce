from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('pedido/', views.list_pedido, name='list_pedido'),
    path('pedido/inserir/', views.ins_pedido, name='ins_pedido'),
    path('pedido/atualizar/<int:pk>', views.upd_pedido, name='upd_pedido'),
    path('pedido/deletar/<int:pk>', views.del_pedido, name='del_pedido'),

    path('pedidoitem/', views.list_pedidoitem, name='list_pedidoitem'),
    path('pedidoitem/inserir/', views.ins_pedidoitem, name='ins_pedidoitem'),
    path('pedidoitem/atualizar/<int:pk>', views.upd_pedidoitem, name='upd_pedidoitem'),
    path('pedidoitem/deletar/<int:pk>', views.del_pedidoitem, name='del_pedidoitem'),
]
    