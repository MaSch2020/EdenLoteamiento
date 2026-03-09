from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "city",
        "department",
        "active",
        "featured",
        "updated_at",
    )
    list_filter = ("active", "featured", "department")
    search_fields = ("name", "city", "department", "address_reference")
    prepopulated_fields = {"slug": ("name",)}