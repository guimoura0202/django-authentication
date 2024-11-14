# auth_site/models.py
from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='game_images/')
    description = models.TextField()

    def __str__(self):
        return self.title

class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]  # 1 a 5

    title = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.author.username}"
