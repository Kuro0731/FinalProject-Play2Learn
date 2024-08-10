from django.db import models
from django.urls import reverse

class Review(models.Model):
    review = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('review:detail', args=[str(self.pk)])

    def __str__(self):
        return self.review
