from django.test import TestCase, Client
from django.urls import reverse
from .models import Category, Product, Service, ServiceInquiry, Testimonial


class StoreViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Laptops", slug="laptops")
        self.product = Product.objects.create(
            name="MacBook Pro 16",
            category=self.category,
            tagline="M3 Pro chip · 18GB Memory",
            price=35000.00,
            condition="brand_new",
            warranty="1 Year Apple Warranty",
            key_features="Liquid Retina XDR\n18GB Unified Memory",
            in_stock=True,
            is_featured=True,
        )
        self.service = Service.objects.create(
            name="Diagnostics & Logic Board Repair",
            slug="diagnostics-repair",
            category="repairs",
            short_description="Precision hardware diagnostics for MacBooks and PCs.",
            full_description="Deep component level inspection.",
            price_starting_at="Free Diagnostic",
            turnaround_time="Same Day",
            icon="wrench",
            is_featured=True,
            order=1,
        )
        self.testimonial = Testimonial.objects.create(
            client_name="Kwame Mensah",
            role_or_location="obuasi,ghana",
            service_rendered="Custom Rig",
            rating=5,
            quote="Great service and warranty.",
        )

    def test_home_view(self):
        response = self.client.get(reverse("catalog:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pristine Hardware")
        self.assertContains(response, "MacBook Pro 16")
        self.assertContains(response, "Logic Board Repair")
        self.assertContains(response, "A.I.M.S")

    def test_product_list_view(self):
        response = self.client.get(reverse("catalog:product_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "MacBook Pro 16")

    def test_product_list_category_filter(self):
        response = self.client.get(reverse("catalog:product_list") + "?category=laptops")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "MacBook Pro 16")

    def test_product_list_condition_filter(self):
        response = self.client.get(reverse("catalog:product_list") + "?condition=brand_new")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "MacBook Pro 16")

    def test_product_list_search(self):
        response = self.client.get(reverse("catalog:product_list") + "?q=MacBook")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "MacBook Pro 16")

    def test_product_detail_view(self):
        response = self.client.get(reverse("catalog:product_detail", args=[self.product.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "MacBook Pro 16")
        self.assertContains(response, "Inquire / Reserve on WhatsApp")
        self.assertContains(response, "1 Year Apple Warranty")
        self.assertContains(response, "Brand New Sealed")

    def test_services_view_get(self):
        response = self.client.get(reverse("catalog:services"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Technical Services & Custom Engineering")
        self.assertContains(response, "Logic Board Repair")

    def test_services_view_post_inquiry(self):
        data = {
            "customer_name": "Ama Serwaa",
            "phone_or_whatsapp": "0240001122",
            "email": "ama@example.com",
            "service_type": "Hardware Diagnostics & Repair",
            "device_model": "MacBook Air M2",
            "issue_or_specs": "Cracked retina display",
            "budget": "GH₵3,500",
        }
        response = self.client.post(reverse("catalog:services"), data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ServiceInquiry.objects.filter(customer_name="Ama Serwaa").exists())
        self.assertContains(response, "Thank you, Ama Serwaa!")

    def test_about_view(self):
        response = self.client.get(reverse("catalog:about"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Honest Hardware. Precision Engineering.")
        self.assertContains(response, "28-Point Diagnostic & QA Inspection")
        self.assertContains(response, "Kwame Mensah")

    def test_contact_view_get_and_post(self):
        response = self.client.get(reverse("catalog:contact"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contact & Store Location")

        post_data = {
            "name": "Kojo Antwi",
            "contact": "0551122334",
            "subject": "Hardware Availability",
            "message": "Do you have the RTX 4080 rig in stock for pickup today?",
        }
        response = self.client.post(reverse("catalog:contact"), post_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ServiceInquiry.objects.filter(customer_name="Kojo Antwi").exists())
        self.assertContains(response, "Thank you, Kojo Antwi!")
