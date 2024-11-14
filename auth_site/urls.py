from django.urls import path
from .views import index, welcome, CustomConfirmEmailView, game_reviews

urlpatterns = [
    path('', index, name='index'),
    path('welcome/', welcome, name='welcome'),    
    path('accounts/confirm-email/<str:key>/', CustomConfirmEmailView.as_view(), name='account_confirm_email'),
]