from django.contrib import admin
from .models import Residue

class ResidueAdmin(admin.ModelAdmin):
    list_display = ["url", "photo"]

admin.site.register(Residue, ResidueAdmin)
