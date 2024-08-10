from django.urls import path

from .views import ReviewDetailView

app_name = 'reviews'
urlpatterns = [
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='detail'),
]