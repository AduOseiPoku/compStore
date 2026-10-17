from django.contrib import admin
from .models import Category, Product, Service, ServiceInquiry, Testimonial


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
        "condition",
        "warranty",
        "in_stock",
        "is_featured",
        "created_at",
    )
    list_filter = ("category", "condition", "in_stock", "is_featured")
    search_fields = ("name", "description", "tagline", "key_features")
    list_editable = ("price", "condition", "in_stock", "is_featured")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price_starting_at",
        "turnaround_time",
        "is_featured",
        "order",
    )
    list_filter = ("category", "is_featured")
    search_fields = ("name", "short_description", "full_description")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("is_featured", "order", "price_starting_at", "turnaround_time")


@admin.register(ServiceInquiry)
class ServiceInquiryAdmin(admin.ModelAdmin):
    list_display = (
        "customer_name",
        "phone_or_whatsapp",
        "service_type",
        "device_model",
        "budget",
        "is_resolved",
        "created_at",
    )
    list_filter = ("service_type", "is_resolved", "created_at")
    search_fields = ("customer_name", "phone_or_whatsapp", "device_model", "issue_or_specs")
    list_editable = ("is_resolved",)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("client_name", "service_rendered", "rating", "verified", "created_at")
    list_filter = ("rating", "verified")
    search_fields = ("client_name", "service_rendered", "quote")
