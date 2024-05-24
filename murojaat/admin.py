from django.contrib import admin
from .models import Murojaat


class MurojaatAdmin(admin.ModelAdmin):
    list_display = ('id', 'fish', 'murojaat_turi', 'status', 'created_at', 'is_read')
    list_filter = ('status', 'created_at')
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Belgilanlarni o'qilgan deb belgilash"

admin.site.register(Murojaat, MurojaatAdmin)
