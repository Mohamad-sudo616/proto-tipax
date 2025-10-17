from django.contrib import admin
from .models import Package

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'ship_type', 'from_location', 'to_location', 'send_date', 'created_at')
    list_filter = ('ship_type', 'send_date', 'created_at')
    search_fields = ('sender__username', 'from_location', 'to_location')
    ordering = ('-created_at',)
