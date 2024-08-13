from django.core.mail import send_mail
from django.conf import settings  # Add this import
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, TemplateView

from .models import ContactUser
from .forms import ContactUsForm

class ContactFormView(SuccessMessageMixin, CreateView):
    model = ContactUser
    form_class = ContactUsForm
    success_url = reverse_lazy('contact:thanks')
    success_message = "Thank you for reaching out. We will get back to you soon."

    def form_valid(self, form):
        # Send the email
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['email']
        send_mail(
            subject,
            message,
            from_email,
            [settings.ADMIN_EMAIL],  # Use settings.ADMIN_EMAIL here
            fail_silently=False,
        )
        return super().form_valid(form)

class ContactThanksView(TemplateView):
    template_name = 'contact/thanks.html'

