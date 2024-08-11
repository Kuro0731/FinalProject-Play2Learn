from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, TemplateView

from .models import ContactUser
from .forms import ContactUsForm

class ContactFormView(SuccessMessageMixin, CreateView):
    model = ContactUser
    form_class = ContactUsForm
    success_url = reverse_lazy('contact:thanks')

class ContactThanksView(TemplateView):
    template_name = 'contact/thanks.html'
