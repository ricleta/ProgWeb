from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django import forms

class SignUpForm(UserCreationForm):
    """
    A custom user creation form that includes an email field and a group selection.
    """
    email = forms.EmailField(max_length=254, required=True, help_text='Obrigatório. Insira um endereço de e-mail válido.')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

class FormularioExemplo(forms.Form):
    """
    A simple example form with a name and email field.
    """
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    search_field = forms.CharField(label='Search', max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Search...', 'type': 'search'}))
    date = forms.DateField(label='Date',input_formats=['%d/%m/%Y', '%Y-%m-%d'],
    help_text='Selecione a data no calendário.',
    error_messages={
        'invalid': 'Por favor, use um dos formatos: DD/MM/AAAA ou AAAA-MM-DD.'
    },
    widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
    )
    cor = forms.CharField(label='Cor', max_length=7, initial="#FF0000", widget=forms.TextInput(attrs={'type': 'color'}))