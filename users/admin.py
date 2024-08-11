from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from common.admin import Play2LearnAdmin

CustomUser = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(Play2LearnAdmin, UserAdmin):
    model = CustomUser

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Optional Fields', {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name'),
        }),
    )
