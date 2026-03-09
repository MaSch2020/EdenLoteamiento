from django.contrib import admin

from .models import Lot


@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "block",
        "number",
        "area_m2",
        "status",
        "price_cash",
        "installment_value",
        "featured",
        "order",
    )
    list_filter = ("project", "status", "featured")
    search_fields = ("project__name", "block", "number")
    ordering = ("project", "order", "block", "number")