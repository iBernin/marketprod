from django.contrib import admin
from . models import MonitorIds

@admin.register(MonitorIds)
class MonitorIdsAdmin(admin.ModelAdmin):
    list_display = "id", "nmId", "price"
    list_display_links = "nmId",