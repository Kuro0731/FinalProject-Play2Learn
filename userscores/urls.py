from django.urls import path

from .views import UserscoreListView

app_name = 'userscores'
urlpatterns = [
    path('', UserscoreListView.as_view(), name='list'),
]