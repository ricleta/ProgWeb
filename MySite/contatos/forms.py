'''
@author: Ricardo
'''
from django import forms
from contatos.models import Pessoa

class ContatoModel2Form(forms.ModelForm):
 dtNasc = forms.DateField(
    widget=forms.DateInput(attrs={'type': 'date'}),
    input_formats=['%d/%m/%Y', '%Y-%m-%d'],
    label='Data do nascimento',
    help_text='Selecione a data no calendário.'
    )
 
 class Meta:
    model = Pessoa
    fields = '__all__'