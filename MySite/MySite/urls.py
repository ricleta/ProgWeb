"""
URL configuration for MySite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, reverse_lazy
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("contatos/", include("contatos.urls")),
    path('', views.IndexView.as_view(), name='home'),
    path('account/', views.HomeSecView.as_view(), name='home-sec'),
    path('account/register/', views.register, name='register'),
    path('account/login/', LoginView.as_view(template_name='MySite/seguranca/login.html'), name='login'),
    path('account/logout/', views.logout, name='logout'),
    path('actual/logout/', LogoutView.as_view(next_page='home-sec'), name='actual-logout'),
    path('account/secret/', views.secret_page, name='secret-page'),
    path('account/password_change/', views.ChangePasswordView.as_view(), name='password_change'),
    path('account/password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('seguranca/password_reset/', PasswordResetView.as_view(
            template_name='MySite/seguranca/password_reset_form.html',
            success_url=reverse_lazy('sec-password_reset_done'),
            html_email_template_name='MySite/seguranca/password_reset_email.html',
            subject_template_name='MySite/seguranca/password_reset_subject.txt',
            from_email='webmaster@meslin.com.br',
        ),
        name='sec-password_reset'
    ),
    path('seguranca/password_reset_done/', PasswordResetDoneView.as_view(
            template_name='MySite/seguranca/password_reset_done.html',
        ),
        name='sec-password_reset_done'
    ),
    path('seguranca/password_reset_confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='MySite/seguranca/password_reset_confirm.html',
            success_url=reverse_lazy('sec-password_reset_complete'),
        ),
        name='password_reset_confirm'
    ),
    path('seguranca/password_reset_complete/', PasswordResetCompleteView.as_view(
            template_name='MySite/seguranca/password_reset_complete.html'
        ),
        name='sec-password_reset_complete'
    ),
    path('formulario/', views.FormularioView.as_view(), name='formulario'),
    path('carros/', include('carros.urls')),
]
