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
        "has_map_geometry_badge",
        "featured",
        "order",
    )
    list_filter = ("project", "status", "featured")
    search_fields = ("project__name", "block", "number")
    ordering = ("project", "order", "block", "number")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "Datos del lote",
            {
                "fields": (
                    "project",
                    ("block", "number"),
                    "area_m2",
                    "status",
                    ("price_cash", "installment_count", "installment_value"),
                )
            },
        ),
        (
            "Mapa",
            {
                "fields": ("map_geometry",),
                "description": (
                    "Puedes pegar aquí el GeoJSON del lote. Recomendado: un Feature con Polygon o MultiPolygon. "
                    "También se acepta una Geometry directa."
                ),
            },
        ),
        (
            "Visualización",
            {
                "fields": (("featured", "order"),),
            },
        ),
        (
            "Auditoría",
            {
                "fields": ("created_at", "updated_at"),
            },
        ),
    )

    @admin.display(boolean=True, description="GeoJSON")
    def has_map_geometry_badge(self, obj):
        return obj.has_map_geometry