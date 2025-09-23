from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

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

@login_required(login_url='login')
def secret_page(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'MySite/privado/secretPage.html')

@login_required(login_url='login')
def logout(request):
    return render(request, 'MySite/seguranca/logout.html')


class ChangePasswordView(PasswordChangeView):
    template_name = 'MySite/seguranca/change_password.html'
    success_url = reverse_lazy('password_change_done')

class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'MySite/seguranca/password_change_done.html'
    success_url = reverse_lazy('home-sec')