from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('categoria/', views.list_categoria, name='list_categoria'),
    path('categoria/inserir/', views.ins_categoria, name='ins_categoria'),
    path('categoria/atualizar/<int:pk>', views.upd_categoria, name='upd_categoria'),
    path('categoria/deletar/<int:pk>', views.del_categoria, name='del_categoria'),

    path('subcategoria/', views.list_subcategoria, name='list_subcategoria'),
    path('subcategoria/inserir/', views.ins_subcategoria, name='ins_subcategoria'),
    path('subcategoria/atualizar/<int:pk>', views.upd_subcategoria, name='upd_subcategoria'),
    path('subcategoria/deletar/<int:pk>', views.del_subcategoria, name='del_subcategoria'),

    path('produto/', views.list_produto, name='list_produto'),
    path('produto/inserir/', views.ins_produto, name='ins_produto'),
    path('produto/atualizar/<int:pk>', views.upd_produto, name='upd_produto'),
    path('produto/deletar/<int:pk>', views.del_produto, name='del_produto'),

    path('produto_variacao/', views.list_produtovariacao, name='list_produtovariacao'),
    path('produto_variacao/inserir/', views.ins_produtovariacao, name='ins_produtovariacao'),
    path('produto_variacao/atualizar/<int:pk>/', views.upd_produtovariacao, name='upd_produtovariacao'),
    path('produto_variacao/deletar/<int:pk>/', views.del_produtovariacao, name='del_produtovariacao'),
]
    