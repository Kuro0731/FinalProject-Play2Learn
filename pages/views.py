from django.views.generic import TemplateView
from reviews.models import Review
class HomePageView(TemplateView):
    template_name = 'pages/home.html'
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        return context