from django.urls import path
from . import views

app_name = "contatos"
urlpatterns = [
    path('lista/', views.ContatoListView.as_view(), name='lista-contatos'),
    path('', views.ContatoListView.as_view(), name='home-contatos'),
]