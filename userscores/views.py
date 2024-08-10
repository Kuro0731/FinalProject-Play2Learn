from django.views.generic import ListView

from .models import Userscore

class UserscoreListView(ListView):
    model = Userscore
