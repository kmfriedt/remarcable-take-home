from django.test import TestCase
from django.urls import reverse

from apps.product.models import Product
from apps.category.models import Category
from apps.product.tests.factories import create_product
from apps.product.tests.factories import create_default_tags


class ProductListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.copper_product = create_product()
        # create copper, indoor, outdoor tags
        cls.tags = create_default_tags()
        cls.copper_product.tags.add(*cls.tags)

        cls.wire_category = Category.objects.create(name="wire")
        cls.aluminum_product = create_product(
            name="aluminum",
            description="aluminum wire outdoor",
            price="100",
            category= cls.wire_category,
        )
        # add outdoor tag the third item in list
        cls.aluminum_product.tags.add(cls.tags[2])

        cls.elec_box_category = Category.objects.create(name="electrical boxes")
        cls.elec_box_product = create_product(
            name="Junction box",
            description="Junction box wire indoor",
            price="99.99",
            category= cls.elec_box_category,
        )
        # add indoor tag second in list
        cls.elec_box_product.tags.add(cls.tags[1])

    def test_product_list_loads(self):
        url = reverse("product-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_returns_all_products_without_filters(self):
        url = reverse("product-list")
        response = self.client.get(url)
        self.assertQuerySetEqual(
            response.context["products"],
            Product.objects.all(),
            ordered=False,
        )

    def test_search_matches_product_name(self):
        url = reverse("product-list")

        response = self.client.get(
            url,
            {"search": "Copper"},
        )

        products = response.context["products"]

        self.assertIn(self.copper_product, products)
        self.assertNotIn(self.aluminum_product, products)
        self.assertNotIn(self.elec_box_product, products)

    def test_search_matches_product_description(self):
        url = reverse("product-list")
        response = self.client.get(
            url,
            {"search": "installations"},
        )
        products = response.context["products"]
        self.assertIn(self.copper_product, products)

    def test_search_is_case_insensitive(self):
        url = reverse("product-list")

        response = self.client.get(
            url,
            {"search": "COPPER"},
        )

        self.assertIn(
            self.copper_product,
            response.context["products"],
        )

        self.assertNotIn(
            self.aluminum_product,
            response.context["products"]
        )

    def test_filter_by_category(self):
        url = reverse("product-list")
        response = self.client.get(
            url,
            {"category": self.elec_box_category.id},
        )

        products = response.context["products"]

        self.assertIn(self.elec_box_product, products)
        self.assertNotIn(self.copper_product, products)
        self.assertNotIn(self.aluminum_product, products)

    def test_filter_by_tag(self):
        url = reverse("product-list")
        copper_tag = self.tags[0]
        response = self.client.get(
            url,
            {"tags": copper_tag.id},
        )

        products = response.context["products"]

        self.assertIn(self.copper_product, products)
        self.assertNotIn(self.aluminum_product, products)
        self.assertNotIn(self.elec_box_product, products)

    def test_filter_by_multiple_tags_uses_and_behavior(self):
        url = reverse("product-list")
        copper_tag = self.tags[0]
        indoor_tag = self.tags[1]
        response = self.client.get(
            url,
            {
                "tags": [copper_tag.id, indoor_tag.id]
            },
        )

        products = response.context["products"]

        self.assertIn(self.copper_product, products)
        self.assertNotIn(self.aluminum_product, products)
        self.assertNotIn(self.elec_box_product, products)