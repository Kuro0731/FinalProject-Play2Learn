from django.contrib import admin

from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review

    # List Attributes
    date_hierarchy = 'updated'
    list_display = ['title', 'review', 'created', 'updated', 'user']
    ordering = ['-updated']

     # Form Attributes
    autocomplete_fields = ['user']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')

        return ()