from django.shortcuts import render, redirect
from cadastro.forms import *

# Create your views here.

def inicio(request):
    dados = []
    dados.append (
        {
            'destaque': 'Destaque',
            'titulo': 'Cabeça Fria Coração Quente',
            'autor': 'Abel Ferreira',
            'trecho': 'Uma viagem pelos bastidores da equipa tecnica: Segredos, reflexões e metodos de trabalho revelados em primeira pessoa.'
        }
    )
    dados.append (
        {
            'destaque': 'Destaque',
            'titulo': 'Python e Django',
            'autor': 'Francisco Marcelo',
            'trecho': 'Desenvolvimento web moderno e ágil.'
        }
    )
    contexto = {
        'dados': dados
    }
    return render(request,'inicio.html', contexto)


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


def visualizar(request):
    lista_emprestimos = Emprestimo.objects.all()
    context = {'lista_emprestimos': lista_emprestimos }
    return render(request,'visualizar.html', context)
     



def editar(request, pk):
    emprestimo = Emprestimo.objects.get(id=pk)
    form = EmprestimoForm(instance= emprestimo)
    context = {'form': form}

    if request.method =='POST':
        form = EmprestimoForm(request.POST, instance= emprestimo)

        if form.is_valid():
            form.save()
            return redirect('cadastro:visualizar')
    return render(request, 'editar.html', context)

def deletar(request, pk):
    emprestimo = Emprestimo.objects.get(id=pk)
    emprestimo.delete()
    return redirect('visualizar')

""" def deletar(request, pk):
    emprestimo = Emprestimo.objects.get(id=pk)
    context = {'emprestimo': emprestimo }

    if request.method =='POST':
        emprestimo.delete()
        return redirect('cadastro:visualizar')
    return render(request, 'deletar.html', context)

 """