from django.db import models
from datetime import date

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cpf = models.CharField(max_length=12, verbose_name='CPF', unique=True)
    email = models.CharField(max_length=50, verbose_name='E-mail')
    telefone = models.CharField(max_length=14, verbose_name='Telefone')

    def __str__(self):
        return f'{self.nome}'
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']


class Livro(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    autor = models.CharField(max_length=50, verbose_name='Autor')
    editora = models.CharField(max_length=50, verbose_name='Editora')
    edicao = models.IntegerField(verbose_name='Edição', default=1)
    observacao = models.TextField(verbose_name='Observação',blank=True)

    def __str__(self):
        return f'{self.titulo.upper()} - {self.autor}'
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['titulo']


class Emprestimo(models.Model):
    
    cliente = models.ForeignKey(Cliente,verbose_name='Nome do Cliente', on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro,verbose_name='Título/Autor do Livro', on_delete=models.CASCADE)
    data_retirada = models.DateField(verbose_name='Data de Retirada') 
    data_entrega_prevista = models.DateField(verbose_name='Previsão para Devolução')
    observacao = models.TextField(verbose_name='Observação', blank=True)
    devolvido = models.BooleanField(verbose_name='Devolvido', blank=True , default=False)
    
    def __str__(self):
        return f'{self.cliente()} - (Livro: {self.livro} - Data Retirada: {self.data_retirada})'
    class Meta:
        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimos'
        ordering = ['cliente']



   

    




