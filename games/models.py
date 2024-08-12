from django.db import models
# Create your models here.
class GameScore(models.Model):
    MATH = "MATH"
    ANAGRAM = "ANAGRAM"
    GAME_CHOICES = [
        (MATH, "Math Facts"),
        (ANAGRAM, "Anagram Hunt")
    ]

    user_name = models.TextField()
    game = models.TextField(choices=GAME_CHOICES, default=MATH)
    settings = models.TextField()
    score = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)