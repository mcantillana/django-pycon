from django.contrib import admin
from contacts.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'message',
        'sender',
    )