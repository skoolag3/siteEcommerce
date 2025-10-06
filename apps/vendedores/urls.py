from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('vendedor/', views.list_vendedor, name='list_vendedor'),
    path('vendedor/inserir/', views.ins_vendedor, name='ins_vendedor'),
    path('vendedor/atualizar/<int:pk>', views.upd_vendedor, name='upd_vendedor'),
    path('vendedor/deletar/<int:pk>', views.del_vendedor, name='del_vendedor'),

    path('empresa/', views.list_empresa, name='list_empresa'),
    path('empresa/inserir/', views.ins_empresa, name='ins_empresa'),
    path('empresa/atualizar/<int:pk>', views.upd_empresa, name='upd_empresa'),
    path('empresa/deletar/<int:pk>', views.del_empresa, name='del_empresa'),
]
    