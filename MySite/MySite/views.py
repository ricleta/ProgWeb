from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class IndexView(TemplateView):
    template_name = 'MySite/index.html'
    success_url = reverse_lazy('home')

class HomeSecView(TemplateView):
    template_name = 'MySite/seguranca/HomeSec.html'
    success_url = reverse_lazy('home-sec')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-sec')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'MySite/seguranca/registro.html', context)
