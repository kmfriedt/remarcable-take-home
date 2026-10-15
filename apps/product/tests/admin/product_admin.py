
from django.contrib import admin
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from apps.product.models import Product
from apps.category.models import Category
from apps.tag.models import Tag


class ProductAdminTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name="wire & cable")
        cls.tag = Tag.objects.create(name="copper")

        cls.product = Product.objects.create(
            name="12 AWG THHN Copper Wire",
            description="Copper wire for electrical installations.",
            price="89.99",
            category=cls.category,
        )
        cls.product.tags.add(cls.tag)

        cls.admin_user = User.objects.create_superuser(
            username="admin",
            password="password123",
        )
    def test_product_admin_page_loads(self):
        self.client.force_login(self.admin_user)

        url = reverse("admin:product_product_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_product_admin_is_registered(self):
        self.assertIn(Product, admin.site._registry)