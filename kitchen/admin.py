from django.contrib import admin
from .models import KitchenTicket


@admin.register(KitchenTicket)
class KitchenTicketAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "status",
        "sent_by",
        "started_at",
        "ready_at",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
        "started_at",
        "ready_at",
    )

    search_fields = (
        "id",
        "order__number",
        "sent_by__name",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "started_at",
        "ready_at",
    )

    ordering = ("-created_at",)