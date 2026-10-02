from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "in_stock", "is_featured", "created_at")
    list_filter = ("category", "in_stock", "is_featured")
    search_fields = ("name", "description", "tagline")
    list_editable = ("price", "in_stock", "is_featured")
