# pylint: disable=missing-module-docstring
from django.db import models
from PIL import Image
from django.conf import settings
import os

#model de produtos
class T_produto(models.Model):         
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to="produto_imagens/%Y%m/", blank=True, null=True)
    slug = models.SlugField(unique=True)
    preco_marketing = models.FloatField()
    preco_marketing_promocional = models.FloatField(default=0)
    tipo = models.CharField(  # Campo apresentado como uma escolha entre simples e variação 
        default="V", max_length=1, choices=(("v", "Variação"), ("s", "Simples"))
    )
    @staticmethod
    def resize_image(img, new_width=800):   # metodo responsável por diminuir o tamanho e a qualidade da imagem passada no model de forma proporcional
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)  # pegando o path da img
        img_pil = Image.open(img_full_path) #abrindo a img na variável img_pil
        original_width, original_height = img_pil.size # largura e altura originais, respectivamente puxadas da variáveç img_pil.size
        if original_width <= new_width: #caso a largura original seja igual a nova largura(800) nada e feito.
            img_pil.close()
            return
        new_height = round((new_width*original_height)/original_width) #calcullo da nova altura. Regra de tres. nova largura(default = 800) está para nova altura(X) assim como altura original está para largura original.
        new_img = img_pil.resize((new_width,new_height),Image.LANCZOS) #resize na nova imagem de acordo com a nova altura. o argumento final Image.LANCZOS é um calculo matematico necessário para redimensionamento de pixels; Existem outros
        new_img.save( #salvando nova imagem de acordo com a função criada 
            img_full_path, #no diretorio da antiga
            opetimize=True, 
            quality=50 # 50% da qualidade
        )
    def save(self, *args, **kwargs): # função save chamada quando algo é salvo 
        super().save(*args, **kwargs)
        if self.imagem: #caso oque foi salvo seja uma imagem 
            max_image_size = 800 
            self.resize_image(self.imagem, max_image_size) # a imagem é colococada na função acima(resize) junto com o max_image_size

    def __str__(self):
        return self.nome
