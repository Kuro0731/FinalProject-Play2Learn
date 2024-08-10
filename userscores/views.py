from django.views.generic import DetailView, ListView

from .models import Userscore

class UserscoreDetailView(DetailView):
    model = Userscore

class UserscoreListView(ListView):
    model = Userscore