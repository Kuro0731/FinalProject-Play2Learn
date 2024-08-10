from django.contrib import admin

from .models import Userscore

@admin.register(Userscore)
class UserscoreAdmin(admin.ModelAdmin):
    model = Userscore
    list_display = ['type', 'settings', 'score', 'time']

    readonly_fields = ('type', 'settings', 'score', 'time')
