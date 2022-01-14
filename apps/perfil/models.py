
from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User
import requests
import json
import re
from utils import validacpf


def dados_uf():
    lista_estados = []
    request = requests.get(
        "https://servicodados.ibge.gov.br/api/v1/localidades/estados")
    request_str = request.text
    request_str = json.loads(request_str)
    for item in request_str:
        lista_tupla = []
        lista_tupla.append(item['sigla'])
        lista_tupla.append(item['nome'])
        tuple(lista_tupla)
        lista_estados.append(lista_tupla)
    return lista_estados


listaestados = dados_uf()


class Perfil(models.Model):
    # one to one field define uma relação de 1 pra um com o elemento do parametro, no caso, o user do django
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2,
                              default='SP',
                              choices=(*listaestados,))

    def __str__(self):
        return f'{self.usuario.first_name} {self.usuario.last_name}'

    def clean(self):
        error_messages = {}
        if not validacpf.valida_cpf(self.cpf):
            error_messages['cpf'] = 'Digite um CPF válido'
        if re.search(r'[^0-9]', self.cep) or len(self.cep) < 8:
            error_messages['cep'] = 'Digite um CEP válido'
        if error_messages:
            raise ValidationError(error_messages)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
