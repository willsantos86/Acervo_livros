from django.shortcuts import render
from cadastro.forms import EmprestimoForm

# Create your views here.
def emprestimo(request):
    sucesso = False
    form = EmprestimoForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'emprestimo.html', contexto)
