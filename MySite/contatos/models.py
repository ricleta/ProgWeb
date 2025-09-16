from django.db import models

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, help_text='Entre o nome')
    idade = models.IntegerField(help_text='Entre a idade')
    salario = models.DecimalField(help_text='Entre o salário', decimal_places=2, max_digits=8)
    email = models.EmailField(help_text='Informe o email', max_length=254)
    telefone = models.CharField(help_text='Telefone com DDD e DDI', max_length=20)
    dtNasc = models.DateField(help_text='Nascimento no formato AAAA-MM-DD', verbose_name='Data de nascimento')
   
    def __str__(self):
        return self.nome

class Endereco(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='enderecos')
    logradouro = models.CharField(max_length=200, help_text='Entre o logradouro')
    cidade = models.CharField(max_length=100, help_text='Entre a cidade')
    estado = models.CharField(max_length=100, help_text='Entre o estado')
    cep = models.CharField(max_length=20, help_text='Entre o CEP')

    def __str__(self):
        return f'{self.logradouro}, {self.cidade} - {self.estado}, {self.cep}'