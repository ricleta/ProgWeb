'''
@author: Ricardo
'''
from django import forms
from contatos.models import Pessoa

class ContatoModel2Form(forms.ModelForm):
 dtNasc = forms.DateField(
    input_formats=['%d/%m/%Y', '%Y-%m-%d'],
    label='Data do nascimento',
    help_text='Selecione a data no calendário.',
    error_messages={
        'invalid': 'Por favor, use um dos formatos: DD/MM/AAAA ou AAAA-MM-DD.'
    },
    )

 class Meta:
    model = Pessoa
    fields = '__all__'
    error_messages = {
        'nome': {
            'required': "O campo nome é obrigatório.",
            'max_length': "O nome não pode ter mais de 100 caracteres.",
        },
        'idade': {
            'invalid': "Por favor, insira um número válido para a idade.",
        },
        'email': {
            'invalid': "O endereço de e-mail informado não é válido.",
        }
    }

 def clean_idade(self):
    """Custom validation to ensure age is a positive number."""
    idade = self.cleaned_data.get('idade')
    # Django's IntegerField already ensures it's a number.
    # We just add our check to ensure it's a positive number.
    if idade is not None and idade <= 0:
        raise forms.ValidationError("A idade deve ser um número positivo.")
    return idade

 def clean_nome(self):
    """Custom validation to ensure the name contains only letters and spaces."""
    nome = self.cleaned_data.get('nome')
    if nome and not all(char.isalpha() or char.isspace() for char in nome):
        raise forms.ValidationError("O nome deve conter apenas letras e espaços.")
    return nome