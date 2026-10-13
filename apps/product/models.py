from django.db import models
from apps.category.models import Category
from apps.tag.models import Tag

from djmoney.models.fields import MoneyField

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = MoneyField(
        max_digits=10,
        decimal_places=2,
        default_currency="CAD",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products",
    )

    tags = models.ManyToManyField(
        Tag,
        related_name="products",
        blank=True,
    )

    def __str__(self):
        return self.name