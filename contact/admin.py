from django.contrib import admin
from .models import ContactUser

@admin.register(ContactUser)
class ContactUserAdmin(admin.ModelAdmin):
    model = ContactUser
    list_display = ['first_name', 'last_name', 'email', 'subject', 'created']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('message', 'created')
        return ()