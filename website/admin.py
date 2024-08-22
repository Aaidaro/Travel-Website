from django.contrib import admin
from website.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'email', 'created_date']
    list_filter = ['email',]
    search_fields = ['subject', "message",]

admin.site.register(Contact, ContactAdmin)