from django.views.generic import ListView, TemplateView, View, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Pessoa, Endereco
from .forms import ContatoModel2Form, EnderecoForm

class IndexView(TemplateView):
    template_name = 'contatos/index.html'
    success_url = reverse_lazy('contatos:home-contatos')


class ContatoListView(ListView):
    model = Pessoa
    context_object_name = 'pessoas'
    template_name = 'contatos/listaContatos.html'

class ContatoCreateView(View):
    template_name = 'contatos/criaContato.html'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests. Renders the template with empty forms.
        """
        pessoa_form = ContatoModel2Form()
        endereco_form = EnderecoForm()
        context = {
            'formulario': pessoa_form,
            'endereco_form': endereco_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests. Processes form data for both Pessoa and Endereco.
        """
        pessoa_form = ContatoModel2Form(request.POST)
        endereco_form = EnderecoForm(request.POST)

        # Check if both forms are valid
        if pessoa_form.is_valid() and endereco_form.is_valid():
            # First, save the Pessoa object to get an instance
            pessoa = pessoa_form.save()

            # Create the Endereco instance but don't save to the DB yet
            endereco = endereco_form.save(commit=False)
            # Link it to the newly created Pessoa
            endereco.pessoa = pessoa
            # Now save the Endereco instance to the database
            endereco.save()

            return redirect(reverse_lazy('contatos:lista-contatos'))
        else:
            # If any form is invalid, re-render the page with the submitted data and errors
            context = {'formulario': pessoa_form, 'endereco_form': endereco_form}
            return render(request, self.template_name, context)

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

class EnderecoCreateView(CreateView):
    model = Endereco
    form_class = EnderecoForm
    template_name = 'contatos/endereco_form.html'
    success_url = reverse_lazy('contatos:lista-contatos')

    def form_valid(self, form):
        # Get the Pessoa object from the URL's 'fk' parameter
        pessoa = Pessoa.objects.get(pk=self.kwargs['fk'])
        # Set the 'pessoa' field of the new Endereco instance before saving
        form.instance.pessoa = pessoa
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['endereco_form'] = context['form']
        # Pass the Pessoa object to the template for a better user experience
        context['pessoa'] = Pessoa.objects.get(pk=self.kwargs['fk'])
        return context

class EnderecoUpdateView(UpdateView):
    model = Endereco
    form_class = EnderecoForm
    template_name = 'contatos/endereco_form.html'
    success_url = reverse_lazy('contatos:lista-contatos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['endereco_form'] = context['form']
        return context

class EnderecoDeleteView(DeleteView):
    model = Endereco
    template_name = 'contatos/endereco_confirm_delete.html'
    success_url = reverse_lazy('contatos:lista-contatos')