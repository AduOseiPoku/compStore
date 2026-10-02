import os
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Seed 100+ robust, realistic hardware products with image URLs and GH₵ pricing"

    def handle(self, *args, **options):
        # 1. Ensure categories exist
        categories_data = [
            {"name": "Laptops", "slug": "laptops"},
            {"name": "Desktops & Workstations", "slug": "desktops"},
            {"name": "Displays & Monitors", "slug": "displays"},
            {"name": "Components & Hardware", "slug": "components"},
            {"name": "Peripherals & Keyboards", "slug": "peripherals"},
            {"name": "Storage & Networking", "slug": "storage-networking"},
            {"name": "Audio & Streaming", "slug": "audio-streaming"},
        ]

        cat_map = {}
        for c in categories_data:
            cat, _ = Category.objects.get_or_create(slug=c["slug"], defaults={"name": c["name"]})
            cat_map[c["slug"]] = cat

        # Curated, reliable high-res tech image URLs on Unsplash CDN
        IMG_LAPTOPS = [
            "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1603302576837-37561b2e2302?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1531297484001-80022131f5a1?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=900&q=80",
        ]

        IMG_DESKTOPS = [
            "https://images.unsplash.com/photo-1587202372775-e229f172b9d7?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1593640408182-31c70c8268f5?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1563770660941-20978e870e26?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1624705002806-5d72df19c3ad?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=900&q=80",
        ]

        IMG_DISPLAYS = [
            "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1547658719-da2b51169166?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1585792180666-f7347c490ee2?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1551645120-d70bfe84c826?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=900&q=80",
        ]

        IMG_COMPONENTS = [
            "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1555680202-c86f0e12f086?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1563770660941-20978e870e26?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1587202372775-e229f172b9d7?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1587202372634-32705e3bf49c?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?auto=format&fit=crop&w=900&q=80",
        ]

        IMG_PERIPHERALS = [
            "https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1541140532154-b024d705b909?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1601445638532-3c6f6c3aa1d6?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1595225476474-87563907a212?auto=format&fit=crop&w=900&q=80",
        ]

        IMG_STORAGE = [
            "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=900&q=80",
        ]

        IMG_AUDIO = [
            "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1546435770-a3e426bf472b?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1583394838336-acd977736f90?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1572536147248-ac59a8abfa4b?auto=format&fit=crop&w=900&q=80",
        ]

        # 105 meticulously curated hardware items
        items = [
            # --- LAPTOPS (20 items) ---
            ("MacBook Pro 16\" M3 Max", "laptops", "Apple M3 Max 16-Core · 40-Core GPU · 64GB RAM · 2TB SSD", 54000.00, IMG_LAPTOPS[0], True, True),
            ("MacBook Pro 14\" M3 Pro", "laptops", "Apple M3 Pro 12-Core · 18-Core GPU · 18GB RAM · 1TB SSD", 32500.00, IMG_LAPTOPS[1], True, False),
            ("MacBook Air 15\" M3", "laptops", "Apple M3 8-Core · 16GB Unified Memory · 512GB SSD · Midnight", 19500.00, IMG_LAPTOPS[2], True, False),
            ("MacBook Air 13\" M3", "laptops", "Apple M3 8-Core · 8GB Unified Memory · 256GB SSD · Starlight", 15200.00, IMG_LAPTOPS[3], True, False),
            ("ThinkPad X1 Carbon Gen 12", "laptops", "Intel Core Ultra 7 155H · 32GB LPDDR5X · 1TB NVMe PCIe 4.0", 28500.00, IMG_LAPTOPS[4], True, True),
            ("ThinkPad P16s Gen 2 Mobile Workstation", "laptops", "AMD Ryzen 7 PRO 7840U · 64GB RAM · 2TB SSD · Radeon 780M", 31000.00, IMG_LAPTOPS[5], True, False),
            ("Dell XPS 16 (2024)", "laptops", "Intel Core Ultra 9 185H · RTX 4070 8GB · 32GB RAM · 4K OLED Touch", 42000.00, IMG_LAPTOPS[6], True, True),
            ("Dell XPS 14 OLED", "laptops", "Intel Core Ultra 7 155H · RTX 4050 6GB · 32GB RAM · 3.2K OLED", 29800.00, IMG_LAPTOPS[7], True, False),
            ("Dell XPS 13 9340", "laptops", "Intel Core Ultra 7 155H · 16GB RAM · 512GB SSD · 120Hz InfinityEdge", 21500.00, IMG_LAPTOPS[8], True, False),
            ("Razer Blade 16 OLED", "laptops", "Intel Core i9-14900HX · RTX 4090 16GB · 32GB DDR5 · 240Hz OLED", 62000.00, IMG_LAPTOPS[9], True, True),
            ("Razer Blade 14 Compact", "laptops", "AMD Ryzen 9 8945HS · RTX 4070 8GB · 32GB DDR5 · 240Hz QHD+", 36500.00, IMG_LAPTOPS[0], True, False),
            ("ASUS ROG Zephyrus G16 OLED", "laptops", "Intel Core Ultra 9 185H · RTX 4080 · 32GB LPDDR5X · 2.5K 240Hz", 41500.00, IMG_LAPTOPS[1], True, False),
            ("ASUS ROG Zephyrus G14", "laptops", "AMD Ryzen 9 8945HS · RTX 4070 · 32GB RAM · 3K OLED 120Hz", 32000.00, IMG_LAPTOPS[2], True, False),
            ("Lenovo Legion Pro 7i Gen 9", "laptops", "Intel Core i9-14900HX · RTX 4080 · 32GB DDR5 · 240Hz WQXGA", 37500.00, IMG_LAPTOPS[3], True, False),
            ("HP Spectre x360 16 2-in-1", "laptops", "Intel Core Ultra 7 155H · RTX 4050 · 32GB RAM · 2.8K OLED Touch", 26500.00, IMG_LAPTOPS[4], True, False),
            ("HP OMEN Transcend 14", "laptops", "Intel Core Ultra 9 185H · RTX 4070 · 32GB RAM · 2.8K 120Hz OLED", 28900.00, IMG_LAPTOPS[5], True, False),
            ("Framework Laptop 16 DIY Edition", "laptops", "AMD Ryzen 7 7840HS · Modular Expansion Cards · 32GB RAM · 1TB SSD", 27000.00, IMG_LAPTOPS[6], True, False),
            ("ASUS Zenbook Duo Dual-Screen", "laptops", "Intel Core Ultra 9 185H · Dual 14\" 3K OLED 120Hz · 32GB RAM", 33500.00, IMG_LAPTOPS[7], True, False),
            ("Acer Predator Helios 18", "laptops", "Intel Core i9-14900HX · RTX 4090 · 32GB DDR5 · 18\" Mini-LED 250Hz", 58000.00, IMG_LAPTOPS[8], True, False),
            ("Microsoft Surface Laptop 7 Copilot+", "laptops", "Snapdragon X Elite 12-Core · 32GB RAM · 1TB SSD · PixelSense Flow", 26000.00, IMG_LAPTOPS[9], True, False),

            # --- DESKTOPS & WORKSTATIONS (15 items) ---
            ("Apple Mac Studio M2 Ultra", "desktops", "24-Core CPU · 76-Core GPU · 128GB Unified Memory · 4TB SSD", 78000.00, IMG_DESKTOPS[0], True, True),
            ("Apple Mac Studio M2 Max", "desktops", "12-Core CPU · 38-Core GPU · 32GB Unified Memory · 512GB SSD", 34500.00, IMG_DESKTOPS[1], True, False),
            ("Apple Mac Mini M2 Pro", "desktops", "10-Core CPU · 16-Core GPU · 16GB Unified Memory · 512GB SSD", 19200.00, IMG_DESKTOPS[2], True, False),
            ("Custom Compact SFF Mini-ITX Rig", "desktops", "AMD Ryzen 9 7900X · RTX 4080 16GB · 32GB DDR5 6000MHz", 38500.00, IMG_DESKTOPS[3], True, True),
            ("Corsair ONE i500 Compact Workstation", "desktops", "Intel Core i9-14900K · Liquid Cooled RTX 4090 · 64GB DDR5 · 4TB NVMe", 72000.00, IMG_DESKTOPS[4], True, True),
            ("Alienware Aurora R16 Gaming Desktop", "desktops", "Intel Core i7-14700F · RTX 4070 Ti Super 16GB · 32GB DDR5 · 1TB SSD", 31500.00, IMG_DESKTOPS[5], True, False),
            ("NZXT Player: Three Prime PC", "desktops", "Intel Core i9-14900KF · RTX 4090 · 64GB DDR5 · 2TB NVMe · Kraken 360", 64500.00, IMG_DESKTOPS[6], True, False),
            ("HP OMEN 45L Cryo-Chamber Tower", "desktops", "Intel Core i9-14900K · RTX 4080 Super · 32GB Kingston FURY · 2TB SSD", 46000.00, IMG_DESKTOPS[7], True, False),
            ("ASUS ROG Strix G16CHR Gaming Rig", "desktops", "Intel Core i7-14700KF · RTX 4070 · 32GB RAM · 1TB PCIe 4.0 SSD", 27000.00, IMG_DESKTOPS[0], True, False),
            ("Lenovo ThinkStation P8 Workstation", "desktops", "AMD Ryzen Threadripper PRO 7965WX · RTX 6000 Ada · 128GB ECC RAM", 125000.00, IMG_DESKTOPS[1], True, False),
            ("Intel NUC 13 Extreme Raptor Canyon", "desktops", "Intel Core i9-13900K · Triple-Slot GPU Ready · 64GB DDR5 · 2TB SSD", 26500.00, IMG_DESKTOPS[2], True, False),
            ("Falcon Northwest FragBox SFF", "desktops", "AMD Ryzen 9 7950X3D · RTX 4090 · 64GB DDR5 · Custom Liquid Cooling", 69000.00, IMG_DESKTOPS[3], True, False),
            ("Dell Precision 3680 Tower", "desktops", "Intel Core i9-14900K · NVIDIA RTX 4000 Ada · 64GB ECC · 2TB NVMe", 48500.00, IMG_DESKTOPS[4], True, False),
            ("Minisforum MS-01 Workstation Mini PC", "desktops", "Intel Core i9-13900H · Dual 10GbE SFP+ · 64GB RAM · 2TB PCIe 4.0", 14800.00, IMG_DESKTOPS[5], True, False),
            ("Beelink SER8 Mini PC", "desktops", "AMD Ryzen 7 8845HS · 32GB DDR5 · 1TB SSD · Radeon 780M · Dual 4K HDMI", 9800.00, IMG_DESKTOPS[6], True, False),

            # --- DISPLAYS & MONITORS (15 items) ---
            ("Apple Studio Display 27\" 5K Retina", "displays", "5120 × 2880 Resolution · 600 nits · True Tone · Studio Mics", 21000.00, IMG_DISPLAYS[0], True, True),
            ("Apple Pro Display XDR 32\" 6K", "displays", "6016 × 3384 · 1600 nits Peak · 1,000,000:1 Contrast · Nano-Texture", 75000.00, IMG_DISPLAYS[1], True, False),
            ("Dell UltraSharp 32\" 4K Video Conferencing Monitor", "displays", "4K IPS Black Panel · 2000:1 Contrast · 90W USB-C Power Delivery", 12500.00, IMG_DISPLAYS[2], True, True),
            ("Dell UltraSharp 40\" Curved WUHD 5K2K", "displays", "5120 × 2160 · 120Hz · IPS Black · Thunderbolt 4 140W Hub", 29500.00, IMG_DISPLAYS[3], True, False),
            ("Samsung Odyssey OLED G9 49\" Curved", "displays", "5120 × 1440 Dual QHD · 240Hz · 0.03ms Response · Neo Quantum Processor", 26000.00, IMG_DISPLAYS[4], True, True),
            ("Samsung Odyssey Neo G8 32\" 4K Mini-LED", "displays", "3840 × 2160 · 240Hz · 1000R Curve · Quantum HDR 2000", 17500.00, IMG_DISPLAYS[5], True, False),
            ("LG UltraFine 32\" OLED Pro 4K", "displays", "3840 × 2160 True RGB OLED · 99% DCI-P3 · 1M:1 Contrast Ratio", 34000.00, IMG_DISPLAYS[6], True, False),
            ("LG UltraGear 34\" Curved OLED 240Hz", "displays", "3440 × 1440 WQHD · 0.03ms · G-Sync Compatible · Anti-Glare Low Reflection", 16800.00, IMG_DISPLAYS[0], True, False),
            ("ASUS ROG Swift OLED PG32UCDM 4K", "displays", "32\" QD-OLED · 4K 240Hz · 0.03ms · Custom Heatsink · USB-C 90W", 23500.00, IMG_DISPLAYS[1], True, False),
            ("ASUS ProArt PA32UCG-K 32\" 4K HDR", "displays", "Mini-LED 1152 Zones · 1600 nits · 120Hz · Hardware Calibrator Included", 44000.00, IMG_DISPLAYS[2], True, False),
            ("BenQ DesignVue PD3220U 32\" 4K", "displays", "Factory Calibrated Delta E ≤ 3 · Thunderbolt 3 Daisy Chain · KVM Switch", 15200.00, IMG_DISPLAYS[3], True, False),
            ("Alienware 34 Curved QD-OLED AW3423DWF", "displays", "165Hz · 0.1ms · Quantum Dot OLED · VESA DisplayHDR True Black 400", 14500.00, IMG_DISPLAYS[4], True, False),
            ("MSI MPG 321URX QD-OLED 4K 240Hz", "displays", "Third-Gen QD-OLED · ClearMR 13000 · Graphene Film Cooling", 18900.00, IMG_DISPLAYS[5], True, False),
            ("Philips Evnia 42\" 4K OLED Gaming Monitor", "displays", "138Hz · HDMI 2.1 · Ambiglow Lighting · Bowers & Wilkins Audio", 19800.00, IMG_DISPLAYS[6], True, False),
            ("ViewSonic ColorPro VP2786-4K", "displays", "100% Adobe RGB · 98% DCI-P3 · ColorPro Wheel Included · Fog Hood", 13200.00, IMG_DISPLAYS[0], True, False),

            # --- COMPONENTS & HARDWARE (15 items) ---
            ("NVIDIA GeForce RTX 4090 Founders Edition", "components", "24GB GDDR6X · Ada Lovelace · 16,384 CUDA Cores · DLSS 3.5", 34500.00, IMG_COMPONENTS[0], True, True),
            ("ASUS ROG Strix GeForce RTX 4080 Super", "components", "16GB GDDR6X · Axial-tech Fans · 3.5-Slot Design · MaxContact", 22500.00, IMG_COMPONENTS[1], True, False),
            ("MSI Gaming X Slim RTX 4070 Ti Super", "components", "16GB GDDR6X · Tri Frozr 3 Cooling · Slim Dual-Slot Bracket", 16200.00, IMG_COMPONENTS[2], True, False),
            ("AMD Radeon RX 7900 XTX", "components", "24GB GDDR6 · RDNA 3 Architecture · DisplayPort 2.1 · AV1 Encode", 17900.00, IMG_COMPONENTS[3], True, False),
            ("AMD Ryzen 9 7950X3D Processor", "components", "16 Cores · 32 Threads · 144MB 3D V-Cache · Up to 5.7GHz Boost", 9800.00, IMG_COMPONENTS[4], True, True),
            ("AMD Ryzen 7 7800X3D Processor", "components", "8 Cores · 16 Threads · Ultimate Gaming CPU · 104MB Cache", 6800.00, IMG_COMPONENTS[5], True, False),
            ("Intel Core i9-14900KS Special Edition", "components", "24 Cores (8P+16E) · 32 Threads · 6.2GHz Max Turbo · Unlocked", 10500.00, IMG_COMPONENTS[6], True, False),
            ("Intel Core i7-14700K Desktop CPU", "components", "20 Cores (8P+12E) · 28 Threads · 5.6GHz Max Turbo · LGA1700", 6400.00, IMG_COMPONENTS[0], True, False),
            ("ASUS ROG Maximus Z790 Dark Hero", "components", "Intel Z790 LGA1700 · PCIe 5.0 · Wi-Fi 7 · Dual Thunderbolt 4", 9500.00, IMG_COMPONENTS[1], True, False),
            ("MSI MEG X670E ACE Motherboard", "components", "AMD AM5 · 22+2+1 Phase VRM · PCIe 5.0 x16 · 10G Super LAN", 11200.00, IMG_COMPONENTS[2], True, False),
            ("Corsair Dominator Titanium RGB 64GB DDR5", "components", "DDR5-6600MHz · CL32 · Hand-Sorted ICs · DHX Cooling", 5200.00, IMG_COMPONENTS[3], True, False),
            ("G.Skill Trident Z5 RGB 32GB DDR5-7200", "components", "Dual Channel Kit (2x16GB) · Intel XMP 3.0 · Brushed Aluminum", 3400.00, IMG_COMPONENTS[4], True, False),
            ("Seasonic Vertex GX-1200 1200W PSU", "components", "ATX 3.0 & PCIe 5.0 Ready · 80 PLUS Gold · 135mm FDB Fan", 4100.00, IMG_COMPONENTS[5], True, False),
            ("Lian Li O11 Dynamic EVO RGB Chassis", "components", "Dual-Chamber Design · Reverse Mode Capable · ARGB Light Strips", 3200.00, IMG_COMPONENTS[6], True, False),
            ("NZXT Kraken Elite 360 RGB Liquid Cooler", "components", "2.36\" Wide-Angle LCD Display · Asetek Gen7 Pump · F120 RGB Core Fans", 4300.00, IMG_COMPONENTS[0], True, False),

            # --- PERIPHERALS & KEYBOARDS (15 items) ---
            ("Keychron Q1 Pro Wireless Custom Keyboard", "peripherals", "Full CNC Machined Aluminum · QMK/VIA Programmable · Gateron Jupiter", 2800.00, IMG_PERIPHERALS[0], True, True),
            ("Keychron Q3 Max Mechanical Keyboard", "peripherals", "Tenkeyless · 2.4GHz + Bluetooth · Acoustic Sound Absorbing Foam", 3100.00, IMG_PERIPHERALS[1], True, False),
            ("Logitech MX Master 3S Ergonomic Mouse", "peripherals", "Quiet Click Tech · 8K DPI Track on Glass · MagSpeed Electromagnetic Scroll", 1400.00, IMG_PERIPHERALS[2], True, True),
            ("Logitech MX Mechanical Wireless Keyboard", "peripherals", "Low-Profile Tactile Quiet Switches · Smart Backlighting · Multi-OS", 2400.00, IMG_PERIPHERALS[3], True, False),
            ("Apple Magic Keyboard with Touch ID & Numeric", "peripherals", "Wireless & Rechargeable · Touch ID Sensor · Space Gray Finish", 2600.00, IMG_PERIPHERALS[4], True, False),
            ("Apple Magic Trackpad (Multi-Touch)", "peripherals", "Edge-to-Edge Glass Surface · Force Touch Sensors · Black Surface", 1950.00, IMG_PERIPHERALS[5], True, False),
            ("SteelSeries Apex Pro TKL Wireless (Gen 3)", "peripherals", "OmniPoint 3.0 Adjustable HyperMagnetic Switches · Rapid Trigger", 3400.00, IMG_PERIPHERALS[6], True, False),
            ("Razer DeathAdder V3 Pro Wireless Mouse", "peripherals", "Focus Pro 30K Optical Sensor · 63g Ultra-Lightweight · HyperPolling 8K", 1900.00, IMG_PERIPHERALS[0], True, False),
            ("Razer Viper Mini Signature Edition", "peripherals", "Magnesium Alloy Exoskeleton · Under 49g · Optical Mouse Switches Gen-3", 4200.00, IMG_PERIPHERALS[1], True, False),
            ("Wooting 60HE+ Analog Keyboard", "peripherals", "Lekker Hall Effect Switches · Rapid Trigger · 0.1mm Actuation Precision", 2950.00, IMG_PERIPHERALS[2], True, False),
            ("NuPhy Air75 V2 Ultra-Slim Wireless", "peripherals", "Gateron Low-Profile Switches · 1000Hz Polling Rate · QMK/VIA Support", 2100.00, IMG_PERIPHERALS[3], True, False),
            ("ZSA Voyager Ergonomic Split Keyboard", "peripherals", "Ultra-Low Profile · Magnetic Tenting Feet · Kailh Choc Hot-Swap", 5600.00, IMG_PERIPHERALS[4], True, False),
            ("Logitech G Pro X Superlight 2 DEX", "peripherals", "HERO 2 Sensor 32K DPI · LIGHTFORCE Hybrid Switches · 60g Ergonomic", 2200.00, IMG_PERIPHERALS[5], True, False),
            ("BenQ ScreenBar Pro Monitor Light Bar", "peripherals", "Auto-Dimming · Ultrawide Illumination · Zero Screen Glare · USB-C", 1850.00, IMG_PERIPHERALS[6], True, False),
            ("CalDigit TS4 Thunderbolt 4 Dock", "peripherals", "18 Ports · 98W Charging · Dual 6K Displays · 2.5 Gigabit Ethernet", 5800.00, IMG_PERIPHERALS[0], True, True),

            # --- STORAGE & NETWORKING (13 items) ---
            ("Samsung 990 PRO 2TB NVMe PCIe 4.0 M.2 SSD", "storage-networking", "7,450 MB/s Sequential Read · 6,900 MB/s Sequential Write", 2600.00, IMG_STORAGE[0], True, True),
            ("Samsung 990 PRO 4TB NVMe SSD with Heatsink", "storage-networking", "4TB Storage · PS5 & PC Ready · Dynamic Thermal Guard", 5400.00, IMG_STORAGE[1], True, False),
            ("Crucial T705 2TB PCIe 5.0 NVMe SSD", "storage-networking", "Blistering 14,500 MB/s Read · Micron 232-Layer TLC NAND", 4800.00, IMG_STORAGE[2], True, False),
            ("WD_BLACK SN850X 2TB NVMe SSD", "storage-networking", "Up to 7,300 MB/s Read · Game Mode 2.0 · Low Latency Loading", 2400.00, IMG_STORAGE[3], True, False),
            ("SanDisk 4TB Extreme PRO Portable SSD", "storage-networking", "Up to 2,000 MB/s Read/Write · IP65 Water & Dust Resistance · USB-C", 4900.00, IMG_STORAGE[4], True, False),
            ("Samsung T9 2TB Portable SSD USB 3.2 Gen 2x2", "storage-networking", "2,000 MB/s Transfer Speed · Drop Resistant up to 3 Meters", 2800.00, IMG_STORAGE[0], True, False),
            ("Synology DiskStation DS923+ 4-Bay NAS", "storage-networking", "AMD Ryzen R1600 · M.2 NVMe SSD Cache Slots · 10GbE Upgradeable", 8900.00, IMG_STORAGE[1], True, True),
            ("Synology 16TB Enterprise SATA HDD HAT5300", "storage-networking", "7,200 RPM · 2.5M Hours MTTF · 512MB Buffer · Sustained 274 MB/s", 5800.00, IMG_STORAGE[2], True, False),
            ("Ubiquiti UniFi Dream Machine Special Edition", "storage-networking", "All-in-One Gateway · Dual WAN (10G SFP+ & 2.5GbE) · Built-in PoE Switch", 7900.00, IMG_STORAGE[3], True, True),
            ("Ubiquiti UniFi U7 Pro Wi-Fi 7 Access Point", "storage-networking", "Tri-Band Wi-Fi 7 · 6 GHz Band · 9.3 Gbps Aggregate Rate · 2.5GbE PoE", 2950.00, IMG_STORAGE[4], True, False),
            ("ASUS ROG Rapture GT-BE98 Quad-Band Wi-Fi 7 Router", "storage-networking", "Up to 30,000 Mbps · Dual 10G Ports · Quad 2.5G Ports · Mobile Game Boost", 9200.00, IMG_STORAGE[0], True, False),
            ("QNAP TS-464-8G 4-Bay Intel Celeron NAS", "storage-networking", "Intel Celeron N5095 Quad-Core · Dual 2.5GbE · M.2 PCIe Gen 3 Slots", 7800.00, IMG_STORAGE[1], True, False),
            ("Seagate IronWolf Pro 20TB NAS Hard Drive", "storage-networking", "AgileArray Technology · 256MB Cache · Rotational Vibration Sensors", 6800.00, IMG_STORAGE[2], True, False),

            # --- AUDIO & STREAMING (12 items) ---
            ("Sony WH-1000XM5 Wireless Headphones", "audio-streaming", "Industry-Leading Active Noise Cancelling · 30-Hour Battery · Auto NC Optimizer", 4800.00, IMG_AUDIO[0], True, True),
            ("Apple AirPods Max (USB-C)", "audio-streaming", "Custom Acoustic Design · Spatial Audio with Dynamic Head Tracking · Active NC", 7900.00, IMG_AUDIO[1], True, True),
            ("Bose QuietComfort Ultra Headphones", "audio-streaming", "World-Class Noise Cancellation · Breakthrough Spatialized Audio · CustomTune", 5200.00, IMG_AUDIO[2], True, False),
            ("Sennheiser HD 660S2 Audiophile Headphones", "audio-streaming", "Open-Back Dynamic · 300-Ohm Transducers · Extended Sub-Bass Response", 7400.00, IMG_AUDIO[3], True, False),
            ("Audio-Technica ATH-M50xBT2 Wireless", "audio-streaming", "Proprietary 45mm Drivers · LDAC Codec Support · 50-Hour Battery Life", 2700.00, IMG_AUDIO[4], True, False),
            ("Shure SM7B Cardioid Dynamic Vocal Mic", "audio-streaming", "Smooth Flat Frequency Response · Bass Rolloff & Midrange Emphasis", 5600.00, IMG_AUDIO[0], True, True),
            ("Shure MV7+ Podcast & Streamer Microphone", "audio-streaming", "Dual XLR/USB-C Hybrid · Customizable LED Touch Panel · Auto Level Mode", 3800.00, IMG_AUDIO[1], True, False),
            ("Elgato Wave:3 Premium USB Condenser Mic", "audio-streaming", "Clipguard Anti-Distortion Tech · 24-bit/96kHz Converter · Wave Link Software", 2150.00, IMG_AUDIO[2], True, False),
            ("Elgato Stream Deck MK.2 (15 LCD Keys)", "audio-streaming", "Customizable LCD Visual Keys · One-Touch App Control · Detachable Stand", 1950.00, IMG_AUDIO[3], True, False),
            ("Elgato Facecam Pro 4K60 Ultra HD Webcam", "audio-streaming", "True 4K at 60 FPS · Sony STARVIS Sensor · Autofocus Studio Lens", 4200.00, IMG_AUDIO[4], True, False),
            ("Focusrite Scarlett 2i2 4th Gen Audio Interface", "audio-streaming", "69dB Ultra-Low Noise Preamps · 120dB Dynamic Range · Auto Gain & Clip Safe", 2800.00, IMG_AUDIO[0], True, False),
            ("Genelec 8010A Compact Studio Monitor (Pair)", "audio-streaming", "Bi-Amplified Active Monitors · Aluminum Enclosure · Precision Sound Staging", 11500.00, IMG_AUDIO[1], True, False),
        ]

        total_seeded = 0
        for name, cat_slug, tagline, price, img_url, in_stock, is_featured in items:
            category = cat_map[cat_slug]
            Product.objects.update_or_create(
                name=name,
                defaults={
                    "category": category,
                    "tagline": tagline,
                    "price": price,
                    "image_url": img_url,
                    "description": f"{tagline}\n\nHigh-performance equipment curated by A.I.M.S. Rigorously tested for hardware reliability and peak throughput.",
                    "in_stock": in_stock,
                    "is_featured": is_featured,
                }
            )
            total_seeded += 1

        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {total_seeded} robust products into A.I.M.S database."))
