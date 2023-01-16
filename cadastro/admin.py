from django.contrib import admin, messages
from cadastro.models import *

@admin.action(description='Marcar emprestimo de livro como devolvido')
def marcar_como_devolvido(modeladmin, request, queryset):
    queryset.update(devolvido=True)
    modeladmin.message_user(request, 'Emprestimo de livros marcado como devolvido', messages.SUCCESS)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'email', 'telefone']
    search_fields = ['nome', 'cpf']
    list_filter = ['nome']
    

class LivroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'editora', 'edicao', 'observacao']
    search_fields = ['autor', 'titulo', 'editora']
    list_filter = ['titulo']

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'livro', 'data_retirada', 'observacao', 'devolvido']
    search_fields = ['cliente', 'livro', 'data_retirada', 'data_entrega']
    list_filter = ['data_retirada', 'devolvido']
    actions = [marcar_como_devolvido]

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Livro, LivroAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
