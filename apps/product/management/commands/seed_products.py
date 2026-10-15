from moneyed import Money

from django.core.management.base import BaseCommand

from apps.product.models import Product
from apps.category.models import Category
from apps.tag.models import Tag

# This code was all written by AI. It helps make it easy to populate the data in the database
# This is the type of things AI should be used for, humans should not spend time writing these types of things out.
# There is zero operational risk to having AI write this code.

class Command(BaseCommand):
    help = "Seed the database with electrical products, categories, and tags."

    categories = [
        "Wire & Cable",
        "Conduit & Fittings",
        "Electrical Boxes",
        "Switches & Receptacles",
        "Circuit Protection",
        "Electrical Panels",
        "Connectors & Terminals",
    ]

    tags = [
        "Commercial",
        "Residential",
        "Indoor",
        "Outdoor",
        "Heavy Duty",
        "Sealed",
        "120V",
        "240V",
        "480V",
        "Copper",
        "Aluminum",
        "Sale",
        "New",
    ]

    products = [
        {
            "name": "12 AWG THHN Copper Wire",
            "description": (
                "12 AWG copper THHN wire suitable for residential and "
                "commercial electrical installations."
            ),
            "price": Money("89.99", "CAD"),
            "category": "Wire & Cable",
            "tags": ["Commercial", "Residential", "Indoor", "Copper", "New"],
        },
        {
            "name": "10 AWG THHN Copper Wire",
            "description": (
                "10 AWG copper THHN wire designed for branch circuits "
                "and general electrical installations."
            ),
            "price": Money("129.99", "CAD"),
            "category": "Wire & Cable",
            "tags": ["Commercial", "Residential", "Indoor", "Copper"],
        },
        {
            "name": "4 AWG Aluminum XHHW-2 Wire",
            "description": (
                "4 AWG aluminum XHHW-2 wire for high-capacity commercial "
                "and industrial electrical installations."
            ),
            "price": Money("249.99", "CAD"),
            "category": "Wire & Cable",
            "tags": ["Commercial", "Outdoor", "Aluminum", "480V"],
        },
        {
            "name": "6/3 Copper MC Cable",
            "description": (
                "6/3 copper metal-clad cable for heavy-duty commercial "
                "electrical applications."
            ),
            "price": Money("319.99", "CAD"),
            "category": "Wire & Cable",
            "tags": ["Commercial", "Indoor", "Copper", "Heavy Duty"],
        },
        {
            "name": '1/2" EMT Conduit',
            "description": (
                "1/2 inch electrical metallic tubing for residential and "
                "commercial indoor installations."
            ),
            "price": Money("12.49", "CAD"),
            "category": "Conduit & Fittings",
            "tags": ["Commercial", "Residential", "Indoor", "120V"],
        },
        {
            "name": '3/4" EMT Compression Coupling',
            "description": (
                "3/4 inch compression coupling for secure connections "
                "between EMT conduit sections."
            ),
            "price": Money("4.99", "CAD"),
            "category": "Conduit & Fittings",
            "tags": ["Commercial", "Indoor", "Heavy Duty"],
        },
        {
            "name": '1" PVC Schedule 40 Conduit',
            "description": (
                "1 inch PVC Schedule 40 conduit for protected outdoor "
                "electrical installations."
            ),
            "price": Money("18.99", "CAD"),
            "category": "Conduit & Fittings",
            "tags": ["Residential", "Outdoor", "Sealed"],
        },
        {
            "name": "Weatherproof Junction Box",
            "description": (
                "Weatherproof junction box designed to protect electrical "
                "connections in demanding outdoor environments."
            ),
            "price": Money("34.99", "CAD"),
            "category": "Electrical Boxes",
            "tags": ["Commercial", "Outdoor", "Sealed", "Heavy Duty"],
        },
        {
            "name": '4" Square Steel Junction Box',
            "description": (
                "Heavy-duty steel junction box for commercial electrical "
                "and wiring installations."
            ),
            "price": Money("9.99", "CAD"),
            "category": "Electrical Boxes",
            "tags": ["Commercial", "Indoor", "Heavy Duty"],
        },
        {
            "name": "Single-Gang PVC Electrical Box",
            "description": (
                "Single-gang PVC electrical box for residential switch "
                "and receptacle installations."
            ),
            "price": Money("3.49", "CAD"),
            "category": "Electrical Boxes",
            "tags": ["Residential", "Indoor", "New"],
        },
        {
            "name": "20A GFCI Receptacle",
            "description": (
                "20 amp GFCI receptacle providing ground-fault protection "
                "for residential and commercial applications."
            ),
            "price": Money("24.99", "CAD"),
            "category": "Switches & Receptacles",
            "tags": ["Residential", "Commercial", "Indoor", "120V", "New"],
        },
        {
            "name": "30A Outdoor Receptacle",
            "description": (
                "30 amp weather-resistant receptacle designed for "
                "outdoor residential electrical installations."
            ),
            "price": Money("29.99", "CAD"),
            "category": "Switches & Receptacles",
            "tags": ["Residential", "Outdoor", "Sealed", "240V"],
        },
        {
            "name": "20A Single-Pole Circuit Breaker",
            "description": (
                "20 amp single-pole circuit breaker for residential "
                "branch circuit protection."
            ),
            "price": Money("14.99", "CAD"),
            "category": "Circuit Protection",
            "tags": ["Residential", "Indoor", "120V", "Sale"],
        },
        {
            "name": "50A Double-Pole Circuit Breaker",
            "description": (
                "50 amp double-pole circuit breaker for residential "
                "and commercial 240 volt applications."
            ),
            "price": Money("39.99", "CAD"),
            "category": "Circuit Protection",
            "tags": ["Residential", "Commercial", "Indoor", "240V"],
        },
        {
            "name": "100A Three-Pole Circuit Breaker",
            "description": (
                "100 amp three-pole circuit breaker for heavy-duty "
                "commercial electrical installations."
            ),
            "price": Money("289.99", "CAD"),
            "category": "Circuit Protection",
            "tags": ["Commercial", "Indoor", "Heavy Duty", "480V"],
        },
        {
            "name": "200A Main Breaker Panel",
            "description": (
                "200 amp main breaker panel designed for residential "
                "and commercial electrical distribution."
            ),
            "price": Money("549.99", "CAD"),
            "category": "Electrical Panels",
            "tags": ["Residential", "Commercial", "Indoor", "240V", "Heavy Duty"],
        },
        {
            "name": "400A Commercial Panelboard",
            "description": (
                "400 amp commercial panelboard for high-capacity "
                "commercial electrical distribution systems."
            ),
            "price": Money("1299.99", "CAD"),
            "category": "Electrical Panels",
            "tags": ["Commercial", "Indoor", "Heavy Duty", "480V", "New"],
        },
        {
            "name": "Copper Compression Lug",
            "description": (
                "Heavy-duty copper compression lug for secure electrical "
                "connections in commercial installations."
            ),
            "price": Money("8.99", "CAD"),
            "category": "Connectors & Terminals",
            "tags": ["Commercial", "Residential", "Copper", "Heavy Duty"],
        },
        {
            "name": "Aluminum Mechanical Lug",
            "description": (
                "Aluminum mechanical lug for reliable connections in "
                "commercial electrical distribution systems."
            ),
            "price": Money("6.99", "CAD"),
            "category": "Connectors & Terminals",
            "tags": ["Commercial", "Aluminum", "240V"],
        },
        {
            "name": "Sealed Wire Connector Kit",
            "description": (
                "Sealed wire connector kit designed to protect electrical "
                "connections from moisture in outdoor installations."
            ),
            "price": Money("19.99", "CAD"),
            "category": "Connectors & Terminals",
            "tags": ["Commercial", "Residential", "Outdoor", "Sealed", "Sale"],
        },
    ]

    def handle(self, *args, **options):
        self.stdout.write("Creating categories...")

        categories = {}

        for category_name in self.categories:
            category, created = Category.objects.get_or_create(
                name=category_name.lower()
            )

            categories[category_name] = category

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"  Created category: {category_name}"
                    )
                )

        self.stdout.write("Creating tags...")

        tags = {}

        for tag_name in self.tags:
            tag, created = Tag.objects.get_or_create(
                name=tag_name.lower()
            )

            tags[tag_name] = tag

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"  Created tag: {tag_name}"
                    )
                )

        self.stdout.write("Creating products...")

        for product_data in self.products:
            product, created = Product.objects.update_or_create(
                name=product_data["name"],
                defaults={
                    "description": product_data["description"],
                    "price": product_data["price"],
                    "category": categories[product_data["category"]],
                },
            )

            product.tags.set(
                [tags[tag] for tag in product_data["tags"]]
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"  Created product: {product.name}"
                    )
                )
            else:
                self.stdout.write(
                    f"  Updated product: {product.name}"
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully seeded {len(self.products)} products."
            )
        )