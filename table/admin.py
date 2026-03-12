from django.contrib import admin
from .models import Table, Category, Product


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "status",
        "is_active",
        "created_at",
    )
    list_filter = (
        "status",
        "is_active",
        "created_at",
    )
    search_fields = (
        "name",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    ordering = ("name",)
    list_per_page = 20


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "is_active",
        "created_at",
    )
    list_filter = (
        "is_active",
        "created_at",
    )
    search_fields = (
        "name",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    ordering = ("name",)
    list_per_page = 20


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "price",
        "is_active",
        "created_at",
    )
    list_filter = (
        "category",
        "is_active",
        "created_at",
    )
    search_fields = (
        "name",
        "kitchen_name",
        "category__name",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    autocomplete_fields = ("category",)
    ordering = ("name",)
    list_per_page = 25

    fieldsets = (
        ("Asosiy ma'lumotlar", {
            "fields": (
                "category",
                "name",
                "kitchen_name",
                "price",
                "is_active",
            )
        }),
        ("Vaqtlar", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )