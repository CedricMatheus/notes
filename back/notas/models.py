'''
BIBLIOTECAS/MÓDULOS
Aqui estamos importando duas bibliotecas que nos auxiliam na definição dos
models.
'''
# importando models do djago
from django.db import models
# importando model de usuario nativo django
from django.contrib.auth.models import User

# definição da classe/model nota
class Nota(models.Model):
    # uma nota pertence a um usuário
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # uma nota possui um título
    titulo = models.CharField(max_length=200)
    # uma nota possui o corpo da nota que chamamos de nota
    nota = models.TextField()
    # uma nota possuí uma data de criação atribuida automaticamente
    data = models.DateTimeField(auto_now_add=True)

    # retorna o título quando o objeto é convertido em string
    def __str__(self):
        return self.titulo