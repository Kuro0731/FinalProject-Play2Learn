from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.safestring import mark_safe

from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken

from common.admin import Play2LearnAdmin
from common.utils.admin import append_fields, move_fields, remove_fields

CustomUser = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(Play2LearnAdmin, UserAdmin):
    model = CustomUser
    
    list_display = UserAdmin.list_display + ('is_superuser',)
    list_display_links = ('username', 'email', 'first_name', 'last_name')

    readonly_fields = ['password_form']

    fieldsets = list(UserAdmin.fieldsets)  

    fieldsets = remove_fields(fieldsets, 'Personal info', ('dob', 'avatar', 'email', 'password'))
    fieldsets = remove_fields(fieldsets, None, ('password_form',))

    fieldsets = append_fields(fieldsets, 'Personal info', ('dob', 'avatar'))
    fieldsets = append_fields(fieldsets, None, ('password_form',))

    fieldsets = move_fields(fieldsets, 'Personal info', None, ('email',))

    add_fieldsets = list(UserAdmin.add_fieldsets)

    add_fieldsets = remove_fields(add_fieldsets, None, ('email', 'first_name', 'last_name', 'dob'))

    add_fieldsets = append_fields(add_fieldsets, None, ('email',))

    add_fieldsets = append_fields(
        add_fieldsets, 'Optional Fields', ('first_name', 'last_name', 'dob')
    )

    def password_form(self, obj):
        url = reverse('admin:auth_user_password_change', args=[obj.pk])
        return mark_safe(f'<a href="{url}">Change Password</a>')

    def get_form(self, request, obj=None, **kwargs):
        self.save_on_top = obj is not None
        return super().get_form(request, obj, **kwargs)

admin.site.unregister(SocialApp)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)

