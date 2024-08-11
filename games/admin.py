from django.contrib import admin
from common.admin import Play2LearnAdmin
from .models import GameScore
@admin.register(GameScore)
class GameScoreAdmin(Play2LearnAdmin):
    model = GameScore

    # List Attributes
    list_display = ['user_name', 'game', 'settings', 'score', 'created']
    ordering = ['-created']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created',)
        return ()