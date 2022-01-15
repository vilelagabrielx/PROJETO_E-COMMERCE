from django.contrib import admin
from .models import Produto, Variacao
from . import models


class VariacaoiIline(admin.TabularInline):
    model = models.Variacao
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'get_preco_formatado',
                    'get_preco_promo_formatado']
    inlines = [
        VariacaoiIline
    ]


admin.site.register(Produto, ProdutoAdmin)

admin.site.register(Variacao)
