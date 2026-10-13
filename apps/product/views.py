from django.db.models import Q
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.decorators.http import require_GET

from apps.product.models import Product
from apps.category.models import Category
from apps.tag.models import Tag

@require_GET
def product_list(request: HttpRequest) -> HttpResponse:
    products = Product.objects.select_related("category").prefetch_related("tags")
    search = request.GET.get("search", "")
    category = request.GET.get("category", "")
    tags = request.GET.getlist("tags", "")

    if search:
        # allow them to search by name or by description
        products = products.filter(
            Q(name__icontains=search) | Q(description__icontains=search)
        )
    if category:
        products = products.filter(category_id=category)

    if tags:
        for tag in tags:
            products = products.filter(tags__id=tag)

    products = products.distinct()

    context = {
        "products": products,
        "categories": Category.objects.all(),
        "tags": Tag.objects.all(),
        "search": search,
        "selected_category": category,
        "selected_tags": tags,
    }

    return render(request, "product_list.html", context)
