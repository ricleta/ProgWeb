from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Pessoa
from .forms import ContatoModel2Form

class IndexView(TemplateView):
    template_name = 'contatos/index.html'
    success_url = reverse_lazy('contatos:home-contatos')


class ContatoListView(ListView):
    model = Pessoa
    context_object_name = 'pessoas'
    template_name = 'contatos/listaContatos.html'

class ContatoCreateView(CreateView):
    model = Pessoa
    form_class = ContatoModel2Form
    template_name = 'contatos/criaContato.html'
    success_url = reverse_lazy('contatos:lista-contatos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formulario'] = context['form']
        return context

class ContatoUpdateView(UpdateView):
    model = Pessoa
    form_class = ContatoModel2Form
    template_name = 'contatos/criaContato.html'
    success_url = reverse_lazy('contatos:lista-contatos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formulario'] = context['form']
        return context

class ContatoDeleteView(DeleteView):
    model = Pessoa
    template_name = 'contatos/contato_confirm_delete.html'
    success_url = reverse_lazy('contatos:lista-contatos')
