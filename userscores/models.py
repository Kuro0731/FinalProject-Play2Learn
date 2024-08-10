from django.db import models
from django.urls import reverse

class Userscore(models.Model):
    score = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('userscore:detail', args=[str(self.pk)])

    def __str__(self):
        return self.score
