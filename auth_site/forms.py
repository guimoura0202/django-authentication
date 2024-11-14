# auth_site/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Review, Game

class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label="Email ou Usuário")
    password = forms.CharField(widget=forms.PasswordInput)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['game', 'title', 'description', 'rating'] 
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'rating': forms.Select(choices=Review.RATING_CHOICES),
        }
        
class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'image', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }