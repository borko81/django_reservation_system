from django.contrib import admin

from . import models

@admin.register(models.OwnerModel)
class OwnerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OwnerBank)
class OwnerBankAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OwnerLastFakIdModel)
class OwnerFakIdAdmin(admin.ModelAdmin):
    pass