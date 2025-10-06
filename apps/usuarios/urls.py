from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("cadastro/", views.cadastro, name="cadastro"),
    path("login/", views.login, name="login"),
    path("logout/", views.user_logout, name="user_logout"),

    path('usuarios/', views.list_user, name='list_user'),
    path('usuarios/inserir/', views.ins_user, name='ins_user'),
    path('usuarios/atualizar/<int:pk>', views.upd_user, name='upd_user'),
    path('usuarios/deletar/<int:pk>', views.del_user, name='del_user'),

    path('endereco/', views.list_endereco, name='list_endereco'),
    path('endereco/inserir/', views.ins_endereco, name='ins_endereco'),
    path('endereco/atualizar/<int:pk>', views.upd_endereco, name='upd_endereco'),
    path('endereco/deletar/<int:pk>', views.del_endereco, name='del_endereco'),
]
    