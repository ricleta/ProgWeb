from django.urls import path
from . import views


app_name = 'carros'

urlpatterns = [
    path("lista/", views.CarsView.as_view(), name='lista-carros'),
]