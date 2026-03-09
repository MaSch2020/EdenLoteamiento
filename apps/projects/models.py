from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    name = models.CharField("Nombre", max_length=150)
    slug = models.SlugField("Slug", max_length=160, unique=True, blank=True)
    city = models.CharField("Ciudad", max_length=120, default="Tomás Romero Pereira")
    department = models.CharField("Departamento", max_length=120, default="Itapúa")
    address_reference = models.CharField(
        "Referencia de dirección",
        max_length=255,
        blank=True,
        default="Tomás Romero Pereira, Itapúa, Paraguay",
    )

    hero_title = models.CharField(
        "Título principal",
        max_length=180,
        default="Tu próximo lote empieza con una decisión clara",
    )
    hero_subtitle = models.TextField(
        "Subtítulo principal",
        default=(
            "Edén Loteamiento presenta una propuesta clara, confiable y fácil "
            "de consultar, con ubicación estratégica y contacto directo."
        ),
    )
    description = models.TextField(
        "Descripción general",
        blank=True,
        default=(
            "Proyecto de loteamiento pensado para comunicar disponibilidad, "
            "ubicación y contacto comercial de forma profesional."
        ),
    )

    latitude = models.DecimalField("Latitud", max_digits=9, decimal_places=6, default=-26.494759)
    longitude = models.DecimalField("Longitud", max_digits=9, decimal_places=6, default=-55.273071)
    map_zoom = models.PositiveSmallIntegerField("Zoom mapa", default=14)

    price_from = models.DecimalField(
        "Precio desde",
        max_digits=12,
        decimal_places=0,
        null=True,
        blank=True,
    )
    installment_from = models.DecimalField(
        "Cuota desde",
        max_digits=12,
        decimal_places=0,
        null=True,
        blank=True,
    )

    whatsapp_number = models.CharField("WhatsApp", max_length=20, blank=True, default="595000000000")
    contact_email = models.EmailField("Correo de contacto", blank=True, default="info@example.com")

    active = models.BooleanField("Activo", default=True)
    featured = models.BooleanField("Destacado", default=True)

    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("Actualizado", auto_now=True)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)