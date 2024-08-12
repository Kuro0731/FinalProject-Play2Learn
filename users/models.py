from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class CustomUser(AbstractUser):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    dob = models.DateField(
        verbose_name="Date of Birth", null=True, blank=True
    )

    def get_absolute_url(self):
        return reverse('my-account')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.username})'