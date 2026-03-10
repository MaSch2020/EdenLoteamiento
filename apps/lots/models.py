from django.core.exceptions import ValidationError
from django.db import models


class Lot(models.Model):
    STATUS_AVAILABLE = "available"
    STATUS_RESERVED = "reserved"
    STATUS_SOLD = "sold"

    STATUS_CHOICES = [
        (STATUS_AVAILABLE, "Disponible"),
        (STATUS_RESERVED, "Reservado"),
        (STATUS_SOLD, "Vendido"),
    ]

    GEOJSON_ALLOWED_TYPES = {
        "Feature",
        "Point",
        "LineString",
        "Polygon",
        "MultiPoint",
        "MultiLineString",
        "MultiPolygon",
        "GeometryCollection",
    }

    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name="lots",
        verbose_name="Proyecto",
    )
    block = models.CharField("Manzana", max_length=20)
    number = models.CharField("Lote", max_length=20)
    area_m2 = models.DecimalField("Superficie (m²)", max_digits=10, decimal_places=2)

    status = models.CharField(
        "Estado",
        max_length=12,
        choices=STATUS_CHOICES,
        default=STATUS_AVAILABLE,
    )

    price_cash = models.DecimalField(
        "Precio contado",
        max_digits=12,
        decimal_places=0,
        null=True,
        blank=True,
    )
    installment_count = models.PositiveIntegerField("Cantidad de cuotas", default=0)
    installment_value = models.DecimalField(
        "Valor de cuota",
        max_digits=12,
        decimal_places=0,
        null=True,
        blank=True,
    )

    map_geometry = models.JSONField(
        "Geometría GeoJSON",
        null=True,
        blank=True,
        help_text=(
            "Pega un objeto GeoJSON válido del lote. Se admite un Feature o una Geometry "
            "(por ejemplo Polygon, MultiPolygon o Point). En GeoJSON el orden de coordenadas "
            "es [longitud, latitud]."
        ),
    )

    featured = models.BooleanField("Destacado en home", default=False)
    order = models.PositiveIntegerField("Orden", default=0)

    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("Actualizado", auto_now=True)

    class Meta:
        verbose_name = "Lote"
        verbose_name_plural = "Lotes"
        ordering = ["order", "block", "number"]
        unique_together = ("project", "block", "number")

    def __str__(self) -> str:
        return f"{self.project.name} - Mz {self.block} Lt {self.number}"

    def clean(self):
        super().clean()
        geometry = self.map_geometry

        if geometry in (None, "", {}):
            return

        if not isinstance(geometry, dict):
            raise ValidationError(
                {"map_geometry": "La geometría del lote debe ser un objeto JSON / GeoJSON válido."}
            )

        geojson_type = geometry.get("type")
        if geojson_type not in self.GEOJSON_ALLOWED_TYPES:
            raise ValidationError(
                {
                    "map_geometry": (
                        "El GeoJSON debe ser un Feature o una geometría válida "
                        f"({', '.join(sorted(self.GEOJSON_ALLOWED_TYPES))})."
                    )
                }
            )

        if geojson_type == "Feature":
            feature_geometry = geometry.get("geometry")
            if not isinstance(feature_geometry, dict):
                raise ValidationError(
                    {"map_geometry": "El Feature GeoJSON debe incluir el objeto 'geometry'."}
                )
            feature_geometry_type = feature_geometry.get("type")
            if feature_geometry_type not in self.GEOJSON_ALLOWED_TYPES - {"Feature"}:
                raise ValidationError(
                    {"map_geometry": "La geometry dentro del Feature no tiene un tipo válido."}
                )
        elif "coordinates" not in geometry and geojson_type != "GeometryCollection":
            raise ValidationError(
                {"map_geometry": "La geometría GeoJSON debe incluir 'coordinates'."}
            )

    @property
    def code(self) -> str:
        return f"MZ-{self.block} / LT-{self.number}"

    @property
    def status_label(self) -> str:
        return dict(self.STATUS_CHOICES).get(self.status, self.status)

    @property
    def has_map_geometry(self) -> bool:
        return bool(self.map_geometry)

    @property
    def map_feature(self) -> dict | None:
        if not self.map_geometry:
            return None

        if self.map_geometry.get("type") == "Feature":
            feature = dict(self.map_geometry)
            feature_properties = dict(feature.get("properties") or {})
            feature_properties.update(self.map_properties)
            feature["properties"] = feature_properties
            return feature

        return {
            "type": "Feature",
            "geometry": self.map_geometry,
            "properties": self.map_properties,
        }

    @property
    def map_properties(self) -> dict:
        return {
            "lot_id": self.pk,
            "project": self.project.name,
            "code": self.code,
            "block": self.block,
            "number": self.number,
            "area_m2": str(self.area_m2),
            "status": self.status,
            "status_label": self.status_label,
            "price_cash": str(self.price_cash) if self.price_cash is not None else None,
            "installment_count": self.installment_count,
            "installment_value": str(self.installment_value) if self.installment_value is not None else None,
        }