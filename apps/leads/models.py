from django.db import models


class Lead(models.Model):
    SOURCE_WEBSITE = "website"
    SOURCE_WHATSAPP = "whatsapp"
    SOURCE_FACEBOOK = "facebook"
    SOURCE_INSTAGRAM = "instagram"
    SOURCE_OTHER = "other"

    SOURCE_CHOICES = [
        (SOURCE_WEBSITE, "Sitio web"),
        (SOURCE_WHATSAPP, "WhatsApp"),
        (SOURCE_FACEBOOK, "Facebook"),
        (SOURCE_INSTAGRAM, "Instagram"),
        (SOURCE_OTHER, "Otro"),
    ]

    STATUS_NEW = "new"
    STATUS_CONTACTED = "contacted"
    STATUS_QUALIFIED = "qualified"
    STATUS_CLOSED = "closed"

    STATUS_CHOICES = [
        (STATUS_NEW, "Nuevo"),
        (STATUS_CONTACTED, "Contactado"),
        (STATUS_QUALIFIED, "Calificado"),
        (STATUS_CLOSED, "Cerrado"),
    ]

    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="leads",
        verbose_name="Proyecto",
    )
    lot = models.ForeignKey(
        "lots.Lot",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="leads",
        verbose_name="Lote de interés",
    )

    full_name = models.CharField("Nombre completo", max_length=150)
    phone = models.CharField("Teléfono", max_length=30)
    email = models.EmailField("Correo", blank=True)
    message = models.TextField("Mensaje", blank=True)

    source = models.CharField(
        "Origen",
        max_length=20,
        choices=SOURCE_CHOICES,
        default=SOURCE_WEBSITE,
    )
    status = models.CharField(
        "Estado",
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_NEW,
    )

    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("Actualizado", auto_now=True)

    class Meta:
        verbose_name = "Lead"
        verbose_name_plural = "Leads"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.full_name} - {self.phone}"