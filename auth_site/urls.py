from django.urls import path
from .views import index, welcome, CustomConfirmEmailView, create_review, create_game, edit_profile

urlpatterns = [
    path('', index, name='index'),
    path('welcome/', welcome, name='welcome'),    
    path('accounts/confirm-email/<str:key>/', CustomConfirmEmailView.as_view(), name='account_confirm_email'),
    path('create-review/', create_review, name='create_review'),
    path('create-game/', create_game, name='create_game'),
    path('edit-profile/', edit_profile, name='edit_profile'),
]