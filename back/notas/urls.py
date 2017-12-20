'''
BIBLIOTECAS/MÓDULOS
Aqui estamos importando duas bibliotecas que nos auxiliam na escrita
das urls.
'''
# importando path
from django.urls import path
# importando views
from . import views

# padrões de url
urlpatterns = [
    # url de login
    path('login/', views.login, name='login'),
    # url de cadastro de usuário
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    # url para listar notas
    path('listar/', views.listar, name='listar'),
    # url para incluir nota
    path('nova/', views.nova, name='nova'),
    # url para carregar nota
    path('carregar/', views.carregar, name='carregar'),
    # url para editar nota
    path('editar/', views.editar, name='editar'),
    # url para deletar nota
    path('deletar/', views.deletar, name='deletar'),
]