from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('avaliacao/', views.list_avaliacao, name='list_avaliacao'),
    path('avaliacao/inserir/', views.ins_avaliacao, name='ins_avaliacao'),
    path('avaliacao/atualizar/<int:pk>', views.upd_avaliacao, name='upd_avaliacao'),
    path('avaliacao/deletar/<int:pk>', views.del_avaliacao, name='del_avaliacao'),

]
    