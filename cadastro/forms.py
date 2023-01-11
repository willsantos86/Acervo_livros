from django import forms
from cadastro.models import Emprestimo


class EmprestimoForm(forms.ModelForm):
    
    class Meta:
        model = Emprestimo
        fields = [
            'cliente', 'livro', 'data_retirada', 'data_entrega_prevista', 'data_entrega', 'observacao'
        ]
        