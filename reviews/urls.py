from django.urls import path
from .views import ReviewDetailView, ReviewListView

app_name = 'reviews'
urlpatterns = [
    path('review/<slug>/', ReviewDetailView.as_view(), name='detail'),
    path('reviews/', ReviewListView.as_view(), name='list'),  # URL for listing reviews
]