from django.contrib import admin
from .models import Trash_can, Zone, Space

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ["id","name","enable"]
    ordering = ("enable", "id")

@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ["get_zone_name","name","enable"]
    ordering = ("enable", "name")
    search_fields = ("name",)
    def get_zone_name(self, obj):
        return obj.zone.name

@admin.register(Trash_can)
class Trash_canAdmin(admin.ModelAdmin):
    list_display = ["name", "get_space_name"]
    ordering = ("enable", "name")
    def get_space_name(self, obj):
        return obj.space.name
