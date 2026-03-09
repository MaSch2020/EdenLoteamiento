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

    @property
    def code(self) -> str:
        return f"MZ-{self.block} / LT-{self.number}"

    @property
    def status_label(self) -> str:
        return dict(self.STATUS_CHOICES).get(self.status, self.status)