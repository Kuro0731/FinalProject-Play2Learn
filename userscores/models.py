from django.db import models
from django.urls import reverse

class Userscore(models.Model):
    type = models.TextField(max_length=100)
    settings = models.TextField(max_length=200)
    score = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.score
