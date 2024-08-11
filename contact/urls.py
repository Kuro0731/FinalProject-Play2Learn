from django.urls import path

from .views import ContactFormView, ContactThanksView

app_name = 'contact'
urlpatterns = [
    path('contact-form/', ContactFormView.as_view(), name='form'),
    path('contact-form/thanks/', ContactThanksView.as_view(), name='thanks'),
]