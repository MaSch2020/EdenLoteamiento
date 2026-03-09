from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "phone",
        "email",
        "project",
        "lot",
        "source",
        "status",
        "created_at",
    )
    list_filter = ("status", "source", "project", "created_at")
    search_fields = ("full_name", "phone", "email", "message")
    readonly_fields = ("created_at", "updated_at")