from django.db import models
from apps.category.models import Category
from apps.tag.models import Tag

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

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