from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cpf = models.CharField(max_length=12, verbose_name='CPF', unique=True)
    email = models.CharField(max_length=50, verbose_name='E-mail')
    telefone = models.CharField(max_length=14, verbose_name='Telefone')

    def __str__(self):
        return f'{self.nome} (Tel: {self.telefone})'


class Livro(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    autor = models.CharField(max_length=50, verbose_name='Autor')
    editora = models.CharField(max_length=50, verbose_name='Editora')
    edicao = models.IntegerField(verbose_name='Edição', default=1)
    observacao = models.TextField(verbose_name='Observação',blank=True)

    def __str__(self):
        return f'{self.titulo.upper()} - (Autor: {self.autor} - Edição: {self.edicao})'


class Emprestimo(models.Model):
    cliente = models.ForeignKey(Cliente,verbose_name='Cliente', on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro,verbose_name='Livro', on_delete=models.CASCADE )
    data_retirada = models.DateField(verbose_name='Data de Retirada') 
    data_entrega = models.DateField(verbose_name='Data de Entrega')
    dias_atraso = models.IntegerField(verbose_name='Dias de Atraso')
    observacao = models.TextField(verbose_name='Observação', blank=True)


