from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import MonitorIds
from users.models import MpUser


@admin.register(MonitorIds)
class MonitorIdsAdmin(admin.ModelAdmin):
    list_display = "id", "nmId", "price"
    list_display_links = "nmId",


@admin.register(MpUser)
class MpUserAdmin(UserAdmin):
    pass
