
from django.contrib import admin
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from apps.product.models import Product
from apps.tag.models import Tag

from apps.product.tests.factories import create_product

class ProductAdminTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tag = Tag.objects.create(name="copper")

        cls.product = create_product()
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