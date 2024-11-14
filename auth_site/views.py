# auth_site/views.py
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomSignupForm, CustomLoginForm, ReviewForm, GameForm, EditProfileForm
from allauth.account.utils import send_email_confirmation
from allauth.account.views import ConfirmEmailView
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from .models import Review, Game

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

    reviews = Review.objects.select_related('game', 'author').order_by('-created_at')  # Ordenar por data de criação
    games = Game.objects.all()  # Obter todos os jogos

    return render(request, 'welcome.html', {
        'user': request.user,
        'reviews': reviews,
        'games': games,  # Adicionar jogos ao contexto
    })

@login_required
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            # review.image = review.game.image  # Não é necessário mais
            review.save()
            messages.success(request, "Review criada com sucesso!")
            return redirect('welcome')
        else:
            messages.error(request, "Corrija os erros no formulário.")
    else:
        form = ReviewForm()
    
    return render(request, 'create_review.html', {'form': form})

@login_required
def create_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save()
            messages.success(request, "Jogo criado com sucesso!")
            return redirect('welcome')
        else:
            messages.error(request, "Corrija os erros no formulário.")
    else:
        form = GameForm()
    
    return render(request, 'create_game.html', {'form': form})

class CustomConfirmEmailView(ConfirmEmailView):
    def get(self, *args, **kwargs):
        confirmation = self.get_object()
        confirmation.confirm(self.request)
        messages.success(self.request, "Seu e-mail foi confirmado com sucesso!")
        return render(self.request, "custom_confirm_email.html", {})
@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('welcome')
        else:
            messages.error(request, "Corrija os erros no formulário.")
    else:
        form = EditProfileForm(instance=user)
    
    return render(request, 'edit_profile.html', {'form': form})