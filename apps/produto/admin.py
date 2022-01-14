from django.contrib import admin
from .models import Produto,Variacao
from . import models



class VariacaoiIline(admin.TabularInline):
    model = models.Variacao
    extra = 1
class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
     VariacaoiIline
    ]
admin.site.register(Produto,ProdutoAdmin)

admin.site.register(Variacao)
