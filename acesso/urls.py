from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('cadastro',views.cadastro, name='cadastro'),
    path('paginaInicial',views.paginaInicial, name='paginaInicial'),
    path('administrador',views.administrador, name='administrador'),
    path('solicita_transporte',views.solicita_transporte, name='solicita_transporte'),   
    path('deferir',views.deferir, name='deferir'), 
    path('editarDados',views.editarDados, name='editarDados'), 
    path('remover/<int:id>', views.remover),
    path('editarstatus/<int:id>', views.editarstatus),
    path('editarDados/<int:id>',views.editarDados)
]
