from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("cadastro/", views.cadastro, name="cadastro"),
    path("login/", views.login, name="login"),
    path("logout/", views.user_logout, name="user_logout"),
]
    