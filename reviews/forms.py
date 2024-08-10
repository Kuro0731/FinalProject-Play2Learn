from django.forms import ModelForm, Textarea, TextInput

from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'review']
        widgets = {
            'title': TextInput(
                attrs={'size': 100, 'autofocus': True}
            ),
            'review': Textarea(
                attrs={'cols': 80, 'rows': 10}
            )
        }
        help_texts = {
            'title': 'Please include what game the review is for.'
        }