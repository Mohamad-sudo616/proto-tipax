# tracking/admin.py
from django.contrib import admin
from .models import Package, PackageEvent

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('tracking_code', 'current_status', 'last_updated')
    search_fields = ('tracking_code',)

@admin.register(PackageEvent)
class PackageEventAdmin(admin.ModelAdmin):
    list_display = ('package', 'status', 'timestamp', 'location')
    list_filter = ('status',)
