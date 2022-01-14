from django.contrib import admin
from .models import *
# Register your models here.
class ItemPedidoInline(admin.TabularInline): #Classe responsável por deixar o item do pedido inline pra coloca-lo junto com o pedido no admin
    model = itemPedido
    extra = 1 #TODO : 'Entender como isso funciona'

class PedidoAdmin(admin.ModelAdmin): #definição da classe do pedido inline passando a classe anterior como argumento
    inlines = [ItemPedidoInline]

admin.site.register(Pedido, PedidoAdmin) #registrando o pedido e o inline do item pedido
admin.site.register(itemPedido)
