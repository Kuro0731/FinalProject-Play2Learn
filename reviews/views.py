from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
from .models import Review
from .forms import ReviewForm
class ReviewCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    success_message = 'Review Created'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ReviewDeleteView(UserPassesTestMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('reviews:list')
    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        return result
    
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Review deleted.')
        return super().form_valid(form)
class ReviewDetailView(DetailView):
    model = Review
class ReviewListView(ListView):
    model = Review
    paginate_by = 1

class ReviewUpdateView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    success_message = 'Review Updated'
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user