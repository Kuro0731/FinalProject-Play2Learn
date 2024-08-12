from django.contrib import admin
from games.models import GameScore

class Play2LearnAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only set user during the first save.
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

class GameScoreAdmin(Play2LearnAdmin):
    model = GameScore

    # List Attributes
    list_display = ['user_name', 'game', 'settings', 'score', 'created']
    list_filter = ['user_name', 'game', 'created']  # Ensure 'created' exists in the model
    ordering = ['-created']
    search_fields = ['user_name', 'game']

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ('created', 'updated')  # Ensure 'created' and 'updated' exist in the model
        return ()

