from django.contrib import admin
from common.admin import Play2LearnAdmin
from .models import Review
@admin.register(Review)
class ReviewAdmin(Play2LearnAdmin):
    model = Review
    # List Attributes
    date_hierarchy = 'updated'
    list_display = ['title', 'review', 'created', 'updated', 'user']
    list_filter = ['user', 'created']
    ordering = ['-updated']
    search_fields = ['user']

    # Form Attributes
    autocomplete_fields = ['user']
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')
        
        return ()