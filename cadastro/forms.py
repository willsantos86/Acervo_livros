from django import forms
from cadastro.models import Emprestimo
from datetime import date

class EmprestimoForm(forms.ModelForm):
    
    def clean_atraso(self):
        data = self.cleaned_data_entrega