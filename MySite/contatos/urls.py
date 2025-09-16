from django.urls import path
from . import views

app_name = "contatos"
urlpatterns = [
    path('cria/', views.ContatoCreateView.as_view(), name='cria-contato'),
    path('update/<int:pk>/', views.ContatoUpdateView.as_view(), name='update-contato'),
    path('delete/<int:pk>/', views.ContatoDeleteView.as_view(), name='delete-contato'),
    path('lista/', views.ContatoListView.as_view(), name='lista-contatos'),
    path('', views.IndexView.as_view(), name='home-contatos'),
    path('update/endereco/<int:pk>/', views.EnderecoUpdateView.as_view(), name='update-endereco'),
    path('delete/endereco/<int:pk>/', views.EnderecoDeleteView.as_view(), name='delete-endereco'),
    path('cria/endereco/<int:fk>/', views.EnderecoCreateView.as_view(), name='cria-endereco'),
]