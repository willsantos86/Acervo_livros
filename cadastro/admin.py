from django.contrib import admin
from cadastro.models import *


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'email', 'telefone']
    search_fields = ['nome', 'cpf']
    list_filter = ['nome']
    

class LivroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'editora', 'edicao', 'observacao']
    search_fields = ['autor', 'titulo', 'editora']
    list_filter = ['titulo']

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'livro', 'data_retirada', 'data_entrega', 'observacao']
    search_fields = ['cliente', 'livro', 'data_retirada', 'data_entrega']
    list_filter = ['data_retirada']

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Livro, LivroAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
