from django.urls import path

from .views import UserscoreDetailView, UserscoreListView

app_name = 'userscores'
urlpatterns = [
    path('userscore/<int:pk>/', UserscoreDetailView.as_view(), name='detail'),
    path('', UserscoreListView.as_view(), name='list'),
]