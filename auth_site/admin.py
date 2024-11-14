# auth_site/admin.py
from django.contrib import admin
from .models import Game, Review

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'game', 'rating', 'created_at')
    list_filter = ('rating', 'game')
    search_fields = ('title', 'description', 'author__username', 'game__title')
