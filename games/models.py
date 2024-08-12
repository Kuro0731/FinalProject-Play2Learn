from django.db import models
# Create your models here.
class GameScore(models.Model):
    MATH = "MATH"
    ANAGRAM = "ANAGRAM"
    GAME_CHOICES = [
        (MATH, "Math Facts"),
        (ANAGRAM, "Anagram Hunt")
    ]

    user_name = models.CharField(max_length=50)
    game = models.TextField(choices=GAME_CHOICES, default=MATH)
    settings = models.CharField(max_length=50)
    score = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.score)

    def get_setting_values(self):
        setting = self.settings
        setting_split = setting.split(",")
        return setting_split