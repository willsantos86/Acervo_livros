from django.contrib import admin
from cadastro.models import *

class ClienteAdmin(admin.ModelAdmin):
    pass

class LivroAdmin(admin.ModelAdmin):
    pass

class EmprestimoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Livro, LivroAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
