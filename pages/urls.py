from django.urls import path

from .views import ContactUsView, HomePageView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
]