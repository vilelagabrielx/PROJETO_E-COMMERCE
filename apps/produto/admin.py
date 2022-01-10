from django.contrib import admin
from .models import T_produto,T_variacao
from . import models



class VariacaoiIline(admin.TabularInline):
    model = models.T_variacao
    extra = 1
class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
     VariacaoiIline
    ]
admin.site.register(T_produto,ProdutoAdmin)

admin.site.register(T_variacao)
