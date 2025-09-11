from django.urls import path
from . import views

app_name = "contatos"
urlpatterns = [
    path('cria/', views.ContatoCreateView.as_view(), name='cria-contato'),
    path('update/<int:pk>/', views.ContatoUpdateView.as_view(), name='update-contato'),
    path('delete/<int:pk>/', views.ContatoDeleteView.as_view(), name='delete-contato'),
    path('lista/', views.ContatoListView.as_view(), name='lista-contatos'),
    path('', views.IndexView.as_view(), name='home-contatos'),
]