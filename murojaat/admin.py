from django.contrib import admin
from .models import Murojaat

class MurojaatAdmin(admin.ModelAdmin):
    list_display = ('fish', 'status', 'created_at', 'is_read')
    list_filter = ('status', 'created_at')
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected letters as read"

admin.site.register(Murojaat, MurojaatAdmin)
