from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Seed demo categories, products, and a default admin user"

    def handle(self, *args, **options):
        # 1. Create or get admin user
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "admin123")
            self.stdout.write(self.style.SUCCESS("Created admin user (username: admin, password: admin123)"))
        else:
            self.stdout.write("Admin user already exists.")

        # 2. Categories
        categories_data = [
            {"name": "Laptops", "slug": "laptops"},
            {"name": "Displays", "slug": "displays"},
            {"name": "Desktops", "slug": "desktops"},
            {"name": "Peripherals", "slug": "peripherals"},
        ]

        cat_map = {}
        for c in categories_data:
            cat, _ = Category.objects.get_or_create(slug=c["slug"], defaults={"name": c["name"]})
            cat_map[c["slug"]] = cat

        # 3. Products (Prices in Ghanaian Cedi GH₵)
        products_data = [
            {
                "name": 'MacBook Pro 16" (Space Black)',
                "category": cat_map["laptops"],
                "tagline": "Apple M3 Pro · 18GB Unified Memory · 512GB SSD",
                "price": 35000.00,
                "description": "Liquid Retina XDR display with ProMotion technology.\nExtreme dynamic range with 1000 nits sustained full-screen brightness.\nUp to 22 hours of battery life with silent thermal design.",
                "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=1000&q=80",
                "in_stock": True,
                "is_featured": True,
            },
            {
                "name": "ThinkPad X1 Carbon Gen 11",
                "category": cat_map["laptops"],
                "tagline": "Intel Core i7-1365U · 32GB LPDDR5 · 1TB NVMe Gen4",
                "price": 22500.00,
                "description": "Ultra-lightweight carbon fiber chassis at 1.12kg.\n14-inch 2.8K OLED anti-glare display with 100% DCI-P3 coverage.\nMil-SPEC tested durability with signature TrackPoint keyboard.",
                "image_url": "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?auto=format&fit=crop&w=1000&q=80",
                "in_stock": True,
                "is_featured": False,
            },
            {
                "name": 'Dell UltraSharp 32" 4K Video Conferencing Monitor',
                "category": cat_map["displays"],
                "tagline": "4K IPS Black Panel · 2000:1 Contrast · 90W USB-C Power Delivery",
                "price": 12500.00,
                "description": "Experience deep blacks and exceptional color contrast with IPS Black technology.\nIntegrated 4K Sony Starvis sensor webcam and echo-canceling dual microphones.\nDaisy-chain capable with dual DisplayPort and RJ45 Ethernet hub.",
                "image_url": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=1000&q=80",
                "in_stock": True,
                "is_featured": True,
            },
            {
                "name": 'Studio Display 27" 5K Retina',
                "category": cat_map["displays"],
                "tagline": "5120 × 2880 Resolution · 600 nits · True Tone · Studio Mics",
                "price": 21000.00,
                "description": "All-aluminum frame with slim profile.\n12MP Ultra Wide camera with Center Stage.\nSix-speaker sound system with Spatial Audio for immersive acoustics.",
                "image_url": "https://images.unsplash.com/photo-1547658719-da2b51169166?auto=format&fit=crop&w=1000&q=80",
                "in_stock": True,
                "is_featured": False,
            },
            {
                "name": "Custom Compact SFF Mini-ITX Rig",
                "category": cat_map["desktops"],
                "tagline": "AMD Ryzen 9 7900X · RTX 4080 16GB · 32GB DDR5 6000MHz",
                "price": 38500.00,
                "description": "Anodized sandblasted aluminum chassis under 11 Liters.\nLiquid cooled with 240mm AIO and PCIe 4.0 riser.\nZero RGB stealth build tuned for maximum performance and silence.",
                "image_url": "https://images.unsplash.com/photo-1587202372775-e229f172b9d7?auto=format&fit=crop&w=1000&q=80",
                "in_stock": True,
                "is_featured": True,
            },
            {
                "name": "Keychron Q1 Pro Wireless Custom Keyboard",
                "category": cat_map["peripherals"],
                "tagline": "Full CNC Machined Aluminum · QMK/VIA Programmable · Gateron Jupiter",
                "price": 2800.00,
                "description": "Double-gasket mount design for refined acoustic feel.\nHot-swappable PCB supporting both 3-pin and 5-pin mechanical switches.\nConnects via Bluetooth 5.1 or USB-C wired mode.",
                "image_url": "https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?auto=format&fit=crop&w=1000&q=80",
                "in_stock": True,
                "is_featured": False,
            },
            {
                "name": "Logitech MX Master 3S Ergonomic Mouse",
                "category": cat_map["peripherals"],
                "tagline": "Quiet Click Tech · 8K DPI Track on Glass · MagSpeed Electromagnetic Scroll",
                "price": 1400.00,
                "description": "Ergonomic silhouette sculpted for palm support.\nQuiet Clicks provide satisfying tactile feel with 90% less click noise.\nCross-computer control with Logitech Flow.",
                "image_url": "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?auto=format&fit=crop&w=1000&q=80",
                "in_stock": True,
                "is_featured": False,
            },
            {
                "name": "Samsung 990 PRO 2TB NVMe PCIe 4.0 M.2 SSD",
                "category": cat_map["peripherals"],
                "tagline": "7,450 MB/s Sequential Read · 6,900 MB/s Sequential Write",
                "price": 2600.00,
                "description": "Flagship solid state drive engineered for heavy gaming, 3D rendering, and 4K video editing.\nNickel-coated controller and smart thermal control algorithm.\nBacked by Samsung Magician Software.",
                "image_url": "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?auto=format&fit=crop&w=1000&q=80",
                "in_stock": True,
                "is_featured": False,
            },
        ]

        for item in products_data:
            Product.objects.update_or_create(
                name=item["name"],
                defaults=item
            )

        self.stdout.write(self.style.SUCCESS(f"Successfully updated {len(products_data)} products with GHS pricing."))

