# auth_site/views.py
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomSignupForm, CustomLoginForm
from allauth.account.utils import send_email_confirmation
from allauth.account.views import ConfirmEmailView
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
def index(request):
    signup_form = CustomSignupForm()
    login_form = CustomLoginForm()

    if request.method == 'POST':
        if 'signup' in request.POST:
            signup_form = CustomSignupForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                # Envia e-mail de confirmação
                send_email_confirmation(request, user)
                messages.info(request, "Cadastro realizado com sucesso! Um e-mail de confirmação foi enviado para você.")
                # Realiza login
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('welcome')
            else:
                messages.error(request, "Corrija os erros no formulário de cadastro.")
        elif 'login' in request.POST:
            login_form = CustomLoginForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('welcome')
            else:
                messages.error(request, "Erro no login. Verifique suas credenciais.")

    return render(request, 'index.html', {
        'signup_form': signup_form,
        'login_form': login_form,
    })

@login_required
def welcome(request):
    if not request.user.emailaddress_set.filter(verified=True).exists():
        messages.warning(request, "Por favor, confirme seu cadastro. Um e-mail de confirmação foi enviado.")
    return render(request, 'welcome.html', {'user': request.user})

class CustomConfirmEmailView(ConfirmEmailView):
    def get(self, *args, **kwargs):
        confirmation = self.get_object()
        confirmation.confirm(self.request)
        messages.success(self.request, "Seu e-mail foi confirmado com sucesso!")
        return render(self.request, "custom_confirm_email.html", {})
