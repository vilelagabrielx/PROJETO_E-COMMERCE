from django.db import models
from PIL import Image
import os


class T_produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to="produto_imagens/%Y%m/", blank=True, null=True)
    slug = models.SlugField(unique=True)
    preco_marketing = models.FloatField()
    preco_marketing_promocional = models.FloatField(default=0)
    tipo = models.CharField(
        default="V", max_length=1, choices=(("v", "Variação"), ("s", "Simples"))
    )
