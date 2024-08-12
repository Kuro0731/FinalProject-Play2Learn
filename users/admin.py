# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from common.admin import Play2LearnAdmin  # Import your custom admin class
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(Play2LearnAdmin, UserAdmin):  # Inherit from Play2LearnAdmin and UserAdmin
    model = CustomUser

    # Add your custom configurations here
    list_display = ['username', 'email', 'created', 'updated']
    readonly_fields = ['created', 'updated']
    ordering = ['-created']
    search_fields = ['username', 'email']

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Optional Fields', {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'dob'),
        }),
    )

