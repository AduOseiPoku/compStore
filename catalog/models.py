from django.db import models
import urllib.parse


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    CONDITION_CHOICES = [
        ("brand_new", "Brand New Sealed"),
        ("open_box", "Open Box (Like New)"),
        ("refurbished_a", "Certified Refurbished (Grade A)"),
        ("refurbished_b", "Refurbished (Grade B)"),
    ]

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )
    name = models.CharField(max_length=200)
    tagline = models.CharField(
        max_length=200,
        blank=True,
        help_text="One-line summary, e.g. 'Apple M3 Pro chip · 18GB Unified Memory'",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(
        max_length=30,
        choices=CONDITION_CHOICES,
        default="brand_new",
        help_text="Device condition tier",
    )
    warranty = models.CharField(
        max_length=120,
        default="6 Months Comprehensive Warranty",
        help_text="Warranty duration and terms included",
    )
    description = models.TextField(blank=True)
    key_features = models.TextField(
        blank=True,
        help_text="Quick bullet highlights (one per line)",
    )
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    image_url = models.URLField(
        blank=True,
        help_text="Optional direct image URL (useful for quick links / unhosted images)",
    )
    in_stock = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-is_featured", "-created_at"]

    def __str__(self):
        return f"{self.name} - GH₵{self.price}"

    @property
    def display_image(self):
        if self.image:
            return self.image.url
        if self.image_url:
            return self.image_url
        return "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=800&q=80"

    @property
    def whatsapp_url(self):
        phone = "233241234567"
        msg = f"Hello A.I.M.S, I'm viewing '{self.name}' (GH₵{self.price:,.2f}, Ref #{self.pk}) on your website. Is it currently in stock for store pickup or delivery?"
        return f"https://wa.me/{phone}?text={urllib.parse.quote(msg)}"

    def get_features_list(self):
        if not self.key_features:
            return []
        return [f.strip() for f in self.key_features.split("\n") if f.strip()]


class Service(models.Model):
    CATEGORY_CHOICES = [
        ("repairs", "Diagnostics & Hardware Repairs"),
        ("custom_pc", "Custom PC Builds & Rigs"),
        ("upgrades", "Component & Speed Upgrades"),
        ("trade_in", "Trade-In & Device Swaps"),
        ("software", "OS, Security & Data Recovery"),
        ("corporate", "Business & Office IT Procurement"),
    ]

    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="repairs")
    short_description = models.CharField(
        max_length=250,
        help_text="Concise 1-2 sentence description for homepage & service cards",
    )
    full_description = models.TextField(
        help_text="Comprehensive details of what is covered, parts used, and guarantee",
    )
    price_starting_at = models.CharField(
        max_length=100,
        default="Free Diagnostic",
        help_text="e.g. 'From GH₵150', 'Diagnostic: Free', 'Custom Quote'",
    )
    turnaround_time = models.CharField(
        max_length=100,
        default="Same Day / 2-4 Hours",
        help_text="e.g. 'Same Day (2-4 hrs)', '24-48 hrs'",
    )
    icon = models.CharField(
        max_length=50,
        default="wrench",
        help_text="Icon identifier: wrench, cpu, swap, shield, hard-drive, server, zap, monitor",
    )
    is_featured = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

    @property
    def whatsapp_url(self):
        phone = "233241234567"
        msg = f"Hello A.I.M.S, I want to inquire about your '{self.name}' service. Could you provide more details or an estimate?"
        return f"https://wa.me/{phone}?text={urllib.parse.quote(msg)}"


class ServiceInquiry(models.Model):
    customer_name = models.CharField(max_length=120)
    phone_or_whatsapp = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    service_type = models.CharField(max_length=100)
    device_model = models.CharField(
        max_length=150,
        blank=True,
        help_text="e.g. MacBook Pro M1 2020, Lenovo Legion 5, or Custom Desktop",
    )
    issue_or_specs = models.TextField(help_text="Describe the issue or desired specifications")
    budget = models.CharField(max_length=100, blank=True, help_text="Optional target budget in GH₵")
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Service Inquiries"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Inquiry from {self.customer_name} ({self.service_type})"


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    role_or_location = models.CharField(max_length=120, blank=True)
    service_rendered = models.CharField(max_length=150, help_text="e.g. Custom RTX 4080 Build or Logic Board Repair")
    rating = models.IntegerField(default=5)
    quote = models.TextField()
    verified = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.client_name} - {self.service_rendered}"
