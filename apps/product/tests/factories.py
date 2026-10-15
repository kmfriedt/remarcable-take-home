from moneyed import Money

from apps.category.models import Category
from apps.product.models import Product
from apps.tag.models import Tag


def create_default_category() -> Category:
    category = Category.objects.create(name="copper")
    return category

def create_default_tags() -> list[Tag]:
    tags = []
    tag_names = ["copper", "indoor", "outdoor"]
    for tag_name in tag_names:
        tag = Tag.objects.create(name=tag_name)
        tags.append(tag)

    return tags

def create_product(
        name: str | None = None,
        description: str | None = None,
        price: str | None = None,
        category: Category | None = None,
) -> Product:
    name = name or "12 AWG THHN Copper Wire"
    description = description or "Copper wire for electrical installations."
    price = price or "89.99"
    category = category or create_default_category()
    money = Money(price, "CAD")
    product = Product.objects.create(
        name=name,
        description=description,
        price=money,
        category=category,
    )
    return product