'''
BIBLIOTECAS/MÓDULOS
Aqui estamos importando algumas bibliotecas que nos auxiliam na composição do
código.
'''
# importando httpresponse
from django.http import HttpResponse
# importando bibliotecas de autenticação
from django.contrib.auth import authenticate
# importando biblioteca json
import json

# função para criar uma resposta httpresponse
def criar_resposta(mensagem):
    # transformando mensagem em json
    mensagem = json.dumps(mensagem)
    # cria um objeto httpresponse a partir da mensagem
    resposta = HttpResponse(mensagem)
    # adiciona cabeçalhos de permissão de requisições cross site
    resposta["Access-Control-Allow-Origin"] = "*"
    resposta["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    resposta["Access-Control-Max-Age"] = "1000"
    resposta["Access-Control-Allow-Headers"] = "*"
    # retorna objeto de resposta
    return resposta


# função para autenticar usuário através da requisição
def autenticar_usuario(requisicao):
    # obtem nome de usuario
    username = requisicao.POST['username']
    # obtem senha
    password = requisicao.POST['password']
    # autentica usuário
    usuario = authenticate(requisicao, username=username, password=password)
    # retorna usuario
    return usuario