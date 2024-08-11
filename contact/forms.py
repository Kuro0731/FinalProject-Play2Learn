from django import forms

from .models import ContactUser

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUser
        fields = (
            'first_name', 'last_name', 'email', 'subject', 'message'
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'autofocus': True}),
            'message': forms.Textarea(attrs={'cols': '100', 'rows': '5'})
        }