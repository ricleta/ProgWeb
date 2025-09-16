from django.views.generic import TemplateView
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'MySite/index.html'
    success_url = reverse_lazy('home')
