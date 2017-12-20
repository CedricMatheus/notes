'''
BIBLIOTECAS/MÓDULOS
Aqui estamos importando algumas bibliotecas que nos auxiliam na escrita
das views.
'''
# importando biblioteca de serializers
from django.core import serializers
# importando biblioteca de csrf_exempt
from django.views.decorators.csrf import csrf_exempt
# importando model de usuário
from django.contrib.auth.models import User
# importando httpresponse
from django.http import HttpResponse
# importando model nota
from .models import Nota
# importando biblioteca de utilidades
import utilidades


# excluindo uso de csrf para a view login
@csrf_exempt
# view login
def login(requisicao):
    # se o metódo da requisição for post
    if requisicao.method == 'POST':
        # autentica usuário
        usuario = utilidades.autenticar_usuario(requisicao)
        # se usuário for autentico
        if usuario is not None:
            # montando mensagem de retorno
            mensagem = {
                # estado da requisição
                'estado': 'sucesso',
                # mensagem
                'mensagem': 'Login efetuado com sucesso!',
                # nome
                'nome': usuario.first_name,
                # nome de usuário
                'username': requisicao.POST['username'],
                # senha do usuário
                'password': requisicao.POST['password'],
            }
        # se usuário não for autentico
        else:
            # montando mensagem de retorno
            mensagem = {
                # estado da requisição
                'estado': 'erro',
                # mensagem
                'mensagem': 'E-mail ou senha inválidos!',
            }
        # cria uma resposta e retorna
        return utilidades.criar_resposta(mensagem)
    # caso requisição não seja post
    else:
        # retorna uma mensagem de acesso restrito
        return HttpResponse('Acesso Restrito!')


# excluindo uso de csrf para a view listar
@csrf_exempt
# view para listar notas de um usuário
def listar(requisicao):
    # se o metódo da requisição for post
    if requisicao.method == 'POST':
        # autentica usuário
        usuario = utilidades.autenticar_usuario(requisicao)
        # se usuário for autentico
        if usuario is not None:
            # obtendo notas do usuário e ordenando por mais recente
            notas = Nota.objects.filter(usuario=usuario).order_by('-data')
            # verificando se existem notas
            if notas:
                # transformando notas em json
                notas = serializers.serialize('json', notas)
                # montando mensagem de retorno
                mensagem = {
                    # estado da requisição
                    'estado': 'sucesso',
                    # mensagem
                    'mensagem': notas,
                }
            # se não existem notas
            else:
                # montando mensagem de retorno
                mensagem = {
                    # estado da requisição
                    'estado': 'vazia',
                    # mensagem
                    'mensagem': 'Não existem notas!'
                }
        # se usuário não for autentico
        else:
            # montando mensagem de retorno
            mensagem = {
                # estado da requisição
                'estado': 'erro',
                # mensagem
                'mensagem': 'Ocorreu um erro inesperado!',
            }
        # cria uma resposta e retorna
        return utilidades.criar_resposta(mensagem)
    # caso requisição não seja post
    else:
        # retorna uma mensagem de acesso restrito
        return HttpResponse('Acesso Restrito!')


# excluindo uso de csrf para a view cadastrar
@csrf_exempt
# view para cadastrar um usuário
def cadastrar(requisicao):
    # se o metódo da requisição for post
    if requisicao.method == 'POST':
        # obtendo nome
        nome = requisicao.POST['nome']
        # obtendo nome de usuário e email
        email = requisicao.POST['email']
        # obtendo senha
        senha = requisicao.POST['senha']
        # tentando criar um usuário
        try:
            # criando usuário
            usuario = User.objects.create_user(email, email, senha)
            # definindo nome do usuário
            usuario.first_name = nome
            # salvando usuário
            usuario.save()
            # montando mensagem de retorno
            mensagem = {
                # estado da requisição
                'estado': 'sucesso',
                # mensagem
                'mensagem': 'Usuário cadastrado com sucesso!',
            }
        # não conseguiu criar usuário
        except:
            # montando mensagem de retorno
            mensagem = {
                # estado da requisição
                'estado': 'erro',
                # mensagem
                'mensagem': 'Ocorreu um erro inesperado!',
            }
            # cria uma resposta e retorna
            return utilidades.criar_resposta(mensagem)
    # caso requisição não seja post
    else:
        # retorna uma mensagem de acesso restrito
        return HttpResponse('Acesso Restrito!')


# excluindo uso de csrf para a view nova
@csrf_exempt
# view para adicionar uma nota
def nova(requisicao):
    # se o metódo da requisição for post
    if requisicao.method == 'POST':
        # autentica usuário
        usuario = utilidades.autenticar_usuario(requisicao)
        # se usuário for autentico
        if usuario is not None:
            # obtendo título da nota
            titulo = requisicao.POST['titulo']
            # obtendo corpo_nota
            corpo_nota = requisicao.POST['nota']
            # criando uma nota na memória
            nota = Nota(usuario=usuario, titulo=titulo, nota=corpo_nota)
            # salvando nota no banco de dados
            nota.save()
            # montando mensagem de retorno
            mensagem = {
                # estado da requisição
                'estado': 'sucesso',
                # mensagem
                'mensagem': 'Nota adicionada com sucesso!',
            }
        # se usuário não for autentico
        else:
            # montando mensagem de retorno
            mensagem = {
                # estado da requisição
                'estado': 'erro',
                # mensagem
                'mensagem': 'Ocorreu um erro inesperado!',
            }
        # cria uma resposta e retorna
        return utilidades.criar_resposta(mensagem)
    # caso requisição não seja post
    else:
        # retorna uma mensagem de acesso restrito
        return HttpResponse('Acesso Restrito!')


# excluindo uso de csrf para a view carregar nota
@csrf_exempt
# view para carregar uma nota
def carregar(requisicao):
    # se o metódo da requisição for post
    if requisicao.method == 'POST':
        # autentica usuário
        usuario = utilidades.autenticar_usuario(requisicao)
        # se usuário for autentico
        if usuario is not None:
            # obtendo título da nota
            id_nota = requisicao.POST['id_nota']
            # obtendo notas do usuário
            notas = Nota.objects.filter(usuario=usuario)
            # tenta obter nota
            try:
                # obtendo nota
                nota = notas.filter(pk=id_nota)
                # transformando nota em json
                nota = serializers.serialize('json', nota)
                # montando mensagem de retorno
                mensagem = {
                    # estado da requisição
                    'estado': 'sucesso',
                    # mensagem
                    'mensagem': nota,
                }
            # não consegue obter nota
            except:
                # montando mensagem de retorno
                mensagem = {
                    # estado da requisição
                    'estado': 'erro',
                    # mensagem
                    'mensagem': 'Ocorreu um erro inesperado!',
                }
        # se usuário não for autentico
        else:
            # montando mensagem de retorno
            mensagem = {
                # estado da requisição
                'estado': 'erro',
                # mensagem
                'mensagem': 'Ocorreu um erro inesperado!',
            }
        # cria uma resposta e retorna
        return utilidades.criar_resposta(mensagem)
    # caso requisição não seja post
    else:
        # retorna uma mensagem de acesso restrito
        return HttpResponse('Acesso Restrito!')


# excluindo uso de csrf para a view editar
@csrf_exempt
# view para editar uma nota
def editar(requisicao):
    # se o metódo da requisição for post
    if requisicao.method == 'POST':
        # autentica usuário
        usuario = utilidades.autenticar_usuario(requisicao)
        # se usuário for autentico
        if usuario is not None:
            # obtendo título da nota
            titulo = requisicao.POST['titulo']
            # obtendo corpo_nota
            corpo_nota = requisicao.POST['nota']
            # obtendo o id da nota
            id_nota = requisicao.POST['id_nota']
            # tenta carregar a nota
            try:
                # busca pela nota do id
                nota = Nota.objects.get(pk=id_nota)
                # verifca se usuário é proprietario da nota
                if nota.usuario == usuario:
                    # alterando titulo
                    nota.titulo = titulo
                    # alterando nota
                    nota.nota = corpo_nota
                    # salvando nota no banco de dados
                    nota.save()
                    # montando mensagem de retorno
                    mensagem = {
                        # estado da requisição
                        'estado': 'sucesso',
                        # mensagem
                        'mensagem': 'Nota editada com sucesso!',
                    }
                # caso usuario não seja proprietário da nota
                else:
                    # montando mensagem de retorno
                    mensagem = {
                        # estado da requisição
                        'estado': 'erro',
                        # mensagem
                        'mensagem': 'Ocorreu um erro inesperado!',
                    }
            # caso não encontre a nota
            except:
                # montando mensagem de retorno
                mensagem = {
                    # estado da requisição
                    'estado': 'erro',
                    # mensagem
                    'mensagem': 'Ocorreu um erro inesperado!',
                }
        # se usuário não for autentico
        else:
            # montando mensagem de retorno
            mensagem = {
                # estado da requisição
                'estado': 'erro',
                # mensagem
                'mensagem': 'Ocorreu um erro inesperado!',
            }
        # cria uma resposta e retorna
        return utilidades.criar_resposta(mensagem)
    # caso requisição não seja post
    else:
        # retorna uma mensagem de acesso restrito
        return HttpResponse('Acesso Restrito!')


# excluindo uso de csrf para a view deletar
@csrf_exempt
# view para deletar uma nota
def deletar(requisicao):
    # se o metódo da requisição for post
    if requisicao.method == 'POST':
        # autentica usuário
        usuario = utilidades.autenticar_usuario(requisicao)
        # se usuário for autentico
        if usuario is not None:
            # obtendo o id da nota
            id_nota = requisicao.POST['id_nota']
            # tenta carregar a nota
            try:
                # busca pela nota do id
                nota = Nota.objects.get(pk=id_nota)
                # verifca se usuário é proprietario da nota
                if nota.usuario == usuario:
                    # deletando nota no banco de dados
                    nota.delete()
                    # montando mensagem de retorno
                    mensagem = {
                        # estado da requisição
                        'estado': 'sucesso',
                        # mensagem
                        'mensagem': 'Nota deletada com sucesso!',
                    }
                # caso usuario não seja proprietário da nota
                else:
                    # montando mensagem de retorno
                    mensagem = {
                        # estado da requisição
                        'estado': 'erro',
                        # mensagem
                        'mensagem': 'Ocorreu um erro inesperado!',
                    }
            # caso não encontre a nota
            except:
                # montando mensagem de retorno
                mensagem = {
                    # estado da requisição
                    'estado': 'erro',
                    # mensagem
                    'mensagem': 'Ocorreu um erro inesperado!',
                }
        # se usuário não for autentico
        else:
            # montando mensagem de retorno
            mensagem = {
                # estado da requisição
                'estado': 'erro',
                # mensagem
                'mensagem': 'Ocorreu um erro inesperado!',
            }
        # cria uma resposta e retorna
        return utilidades.criar_resposta(mensagem)
    # caso requisição não seja post
    else:
        # retorna uma mensagem de acesso restrito
        return HttpResponse('Acesso Restrito!')