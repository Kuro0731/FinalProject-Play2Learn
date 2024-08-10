from django.db import models

class Userscore(models.Model):
    score = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.score
