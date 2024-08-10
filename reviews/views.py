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
    success_message = 'Review Deleted'

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
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        order_fields, order_key, direction = self.get_order_settings()

        context['order'] = order_key
        context['direction'] = direction

        # get all but the last order key, which is 'default'
        context['order_fields'] = list(order_fields.keys())[:-1]

        return context

    def get_ordering(self):
        order_fields, order_key, direction = self.get_order_settings()

        ordering = order_fields[order_key]

        # if direction is 'desc' or is invalid use descending order
        if direction != 'asc':
            ordering = '-' + ordering

        return ordering

    def get_order_settings(self):
        order_fields = self.get_order_fields()
        default_order_key = order_fields['default_key']
        order_key = self.request.GET.get('order', default_order_key)
        direction = self.request.GET.get('direction', 'desc')

        # if order_key is invalid, use default
        if order_key not in order_fields:
            order_key = default_order_key

        return (order_fields, order_key, direction)

    def get_order_fields(self):
        # Returns a dict mapping friendly name sto field names and lookups.
        return {
            'title': 'title',
            'review': 'review',
            'creator': 'user__username',
            'created': 'created',
            'updated': 'updated',
            'default_key': 'updated'
        }

    def get_queryset(self):
        ordering = self.get_ordering()
        qs = Review.objects.all()

        if 'q' in self.request.GET: # Filter by search query
            q = self.request.GET.get('q')
            qs = qs.filter(
                Q(title__icontains=q) | Q(review__icontains=q)
            )

        return qs.order_by(ordering)

class ReviewUpdateView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    success_message = 'Review Updated'

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user