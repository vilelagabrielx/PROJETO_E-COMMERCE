import requests
import json


# def dados_uf():
#     lista_estados = []
#     request = requests.get(
#         "https://servicodados.ibge.gov.br/api/v1/localidades/estados")
#     request_str = request.text
#     request_str = json.loads(request_str)
#     print(request_str[0])
#     for item in request_str:
#         lista_tupla = []
#         lista_tupla.append(item['sigla'])
#         lista_tupla.append(item['nome'])
#         tuple(lista_tupla)
#         lista_estados.append(lista_tupla)
#     return lista_estados


dados_uf()
