from django.contrib import admin

from rooms.models import *

@admin.register(FloorModel)
class FloorAdmin(admin.ModelAdmin):
    pass

@admin.register(BedModel)
class BedsAdmin(admin.ModelAdmin):
    pass
