from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from catalog.models import Category, Product, Service, Testimonial


class Command(BaseCommand):
    help = "Seed demo categories, products, services, testimonials, and default admin"

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

        # 3. Products
        products_data = [
            {
                "name": 'MacBook Pro 16" (Space Black)',
                "category": cat_map["laptops"],
                "tagline": "Apple M3 Pro · 18GB Unified Memory · 512GB SSD",
                "price": 35000.00,
                "condition": "brand_new",
                "warranty": "1 Year Official Apple Warranty",
                "key_features": "Liquid Retina XDR 120Hz ProMotion\nApple M3 Pro 12-core CPU / 18-core GPU\n100% Battery Health with MagSafe 3 Fast Charging\nThunderbolt 4, HDMI 2.1 & SDXC slot",
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
                "condition": "open_box",
                "warranty": "6 Months Comprehensive Store Warranty",
                "key_features": "Ultralight 1.12kg Carbon Fiber Chassis\n14-inch 2.8K OLED Display 100% DCI-P3\nIntel Iris Xe Graphics\nFingerprint reader & IR facial unlock",
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
                "condition": "brand_new",
                "warranty": "1 Year Manufacturer Replacement Guarantee",
                "key_features": "4K UHD 3840x2160 IPS Black Technology\nBuilt-in 4K Sony Starvis Sensor Webcam\n90W USB-C One-Cable Laptop Charging Hub\nRJ45 Ethernet & Dual DisplayPort Daisy Chaining",
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
                "condition": "refurbished_a",
                "warranty": "6 Months Store Warranty",
                "key_features": "5K 5120 x 2880 Retina Resolution (14.7 Million Pixels)\n12MP Ultra-Wide Camera with Center Stage\nSix-Speaker Sound System with Spatial Audio\nTilt-adjustable Aluminum Stand",
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
                "condition": "brand_new",
                "warranty": "1 Year Workshop Assembly & Parts Warranty",
                "key_features": "FormD T1 Sandblasted Anodized Aluminum 10L Case\nNVIDIA GeForce RTX 4080 Founders Edition\n240mm Custom Silent Liquid Cooler\nCorsair SF750 Platinum Modular Power Supply",
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
                "condition": "brand_new",
                "warranty": "6 Months Warranty",
                "key_features": "Solid CNC Anodized Aluminum Body\nDouble-Gasket Acoustic Dampened Design\nHot-Swappable 5-Pin Switch Sockets\nBluetooth 5.1 & Type-C Wired Modes",
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
                "condition": "brand_new",
                "warranty": "6 Months Replacement Warranty",
                "key_features": "8,000 DPI Optical Sensor Works on Any Surface\nQuiet Click Tactile Switches\nMagSpeed Wheel scrolls 1,000 lines in 1 second\nUp to 70 days battery life on full charge",
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
                "condition": "brand_new",
                "warranty": "1 Year Direct Replacement Warranty",
                "key_features": "Blazing 7,450 MB/s Read & 6,900 MB/s Write\nSamsung In-House Nickel-Coated Controller\nPS5 Compatible & High-End PC Ready\nDynamic Thermal Guard Technology",
                "description": "Flagship solid state drive engineered for heavy gaming, 3D rendering, and 4K video editing.\nNickel-coated controller and smart thermal control algorithm.\nBacked by Samsung Magician Software.",
                "image_url": "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?auto=format&fit=crop&w=1000&q=80",
                "in_stock": True,
                "is_featured": False,
            },
        ]

        for item in products_data:
            Product.objects.update_or_create(
                name=item["name"],
                defaults=item,
            )

        # 4. Services
        services_data = [
            {
                "name": "Hardware Diagnostic & Repair Lab",
                "slug": "hardware-diagnostics-repair",
                "category": "repairs",
                "icon": "wrench",
                "short_description": "Precision diagnostics for laptops, MacBooks & desktop motherboards. We fix broken displays, failing batteries, charging ports, and liquid damage.",
                "full_description": "Our bench technicians diagnose hardware faults down to the board level. We use digital microscopes, multimeter tracing, and genuine replacement displays, batteries, and charging ports. Every repair goes through thermal testing and a 30-day post-service warranty.",
                "price_starting_at": "Free Initial Diagnostic",
                "turnaround_time": "Same-Day to 24 Hours",
                "is_featured": True,
                "order": 1,
            },
            {
                "name": "Custom PC Rig Building & Workstations",
                "slug": "custom-pc-builds",
                "category": "custom_pc",
                "icon": "cpu",
                "short_description": "Bespoke desktop assemblies engineered for high-FPS gaming, 3D rendering, video editing, architecture, and AI machine learning workloads.",
                "full_description": "Tell us your software requirements and budget, and we hand-select balanced components with zero bottlenecking. We handle clean cable routing, BIOS flashing, memory XMP/EXPO overclocking, fan curves, and a 24-hour FurMark and Prime95 stress test.",
                "price_starting_at": "Custom Quote (From GH₵8,000+)",
                "turnaround_time": "24 to 48 Hours",
                "is_featured": True,
                "order": 2,
            },
            {
                "name": "Performance Upgrades & Thermal Tuning",
                "slug": "performance-thermal-tuning",
                "category": "upgrades",
                "icon": "zap",
                "short_description": "High-speed NVMe SSD installations, RAM expansions, and premium Arctic MX-6 / Thermal Grizzly repasting to stop laptop overheating.",
                "full_description": "Is your laptop throttling, running hot, or running out of storage? We clone your current system byte-for-byte to a new lightning-fast Gen4 NVMe SSD, expand RAM for multitasking, and clean out accumulated dust with high-end thermal compound.",
                "price_starting_at": "From GH₵250 + Parts",
                "turnaround_time": "1 to 2 Hours (While You Wait)",
                "is_featured": True,
                "order": 3,
            },
            {
                "name": "Device Trade-In & Upgrade Program",
                "slug": "device-trade-in",
                "category": "trade_in",
                "icon": "swap",
                "short_description": "Bring in your old MacBook, Windows laptop, or PC parts and instantly deduct their cash value towards a newer, more powerful machine.",
                "full_description": "No waiting for buyers online. Bring your device to our obuasi,ghana workshop, our technician evaluates its screen, battery, and specs in 15 minutes, and you get an instant discount voucher or cash trade-in towards any in-stock hardware.",
                "price_starting_at": "Instant Valuation in 15 Mins",
                "turnaround_time": "Immediate In-Store",
                "is_featured": True,
                "order": 4,
            },
            {
                "name": "Clean OS Setup & Secure Data Recovery",
                "slug": "os-data-recovery",
                "category": "software",
                "icon": "shield",
                "short_description": "Professional macOS / Windows 11 clean installations, driver optimization, corrupted drive data recovery, and corporate malware cleanup.",
                "full_description": "We perform byte-level file recovery from damaged or unreadable hard drives and SSDs, clean reinstallation of operating systems without bloatware, and seamless data transfer between old and new computers.",
                "price_starting_at": "From GH₵180",
                "turnaround_time": "Same-Day (2-5 Hours)",
                "is_featured": False,
                "order": 5,
            },
            {
                "name": "Corporate & Enterprise IT Procurement",
                "slug": "corporate-procurement",
                "category": "corporate",
                "icon": "briefcase",
                "short_description": "Bulk hardware sourcing, office workstation setups, multi-monitor ergonomics, and maintenance service agreements for startups and offices.",
                "full_description": "Equip your engineering, creative, or administrative teams with pre-configured laptops and displays. We provide official VAT invoices, warranty tracking, on-site setup, and prioritized emergency repair turnarounds.",
                "price_starting_at": "Tailored Business Pricing",
                "turnaround_time": "Scheduled Contract",
                "is_featured": False,
                "order": 6,
            },
        ]

        for s in services_data:
            Service.objects.update_or_create(
                slug=s["slug"],
                defaults=s,
            )

        # 5. Testimonials
        testimonials_data = [
            {
                "client_name": "Kofi Mensah",
                "role_or_location": "3D Animator & Motion Designer · obuasi,ghana",
                "service_rendered": "Custom Ryzen 9 + RTX 4080 Render Workstation",
                "rating": 5,
                "quote": "A.I.M.S built my rendering workstation from scratch in under 48 hours. The cable management was pristine, temperatures stay under 65°C under full Blender load, and they even stress-tested it before dispatch. Best tech team in obuasi,ghana hands down.",
                "verified": True,
            },
            {
                "client_name": "Naa Adjeley",
                "role_or_location": "Architect · obuasi,ghana",
                "service_rendered": "MacBook Pro M1 Display & Battery Replacement",
                "rating": 5,
                "quote": "I cracked my MacBook screen on a Tuesday and had a client presentation on Thursday. Other shops told me 2 weeks for parts. A.I.M.S had the genuine Retina assembly in stock and replaced it same day with a 6-month warranty. Life savers!",
                "verified": True,
            },
            {
                "client_name": "Emmanuel Quaye",
                "role_or_location": "Full Stack Dev · obuasi,ghana",
                "service_rendered": "ThinkPad Trade-In & RAM/SSD Upgrade",
                "rating": 5,
                "quote": "Traded in my older T480 and got a solid valuation towards an X1 Carbon. The WhatsApp communication was instantaneous and transparent. No shady haggling.",
                "verified": True,
            },
        ]

        for t in testimonials_data:
            Testimonial.objects.update_or_create(
                client_name=t["client_name"],
                defaults=t,
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded products, services, and testimonials!"))
