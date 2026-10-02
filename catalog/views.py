from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Product, Category


def product_list(request):
    categories = Category.objects.all()
    selected_category = request.GET.get("category", "").strip()
    query = request.GET.get("q", "").strip()

    products = Product.objects.all()

    if selected_category:
        products = products.filter(category__slug=selected_category)

    if query:
        products = products.filter(
            Q(name__icontains=query)
            | Q(tagline__icontains=query)
            | Q(description__icontains=query)
        )

    total_count = products.count()

    # Minimalist pagination: 24 items per page
    paginator = Paginator(products, 24)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "products": page_obj.object_list,
        "categories": categories,
        "selected_category": selected_category,
        "query": query,
        "total_items": total_count,
    }
    return render(request, "catalog/product_list.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.exclude(pk=pk).filter(category=product.category)[:4]

    context = {
        "product": product,
        "related_products": related_products,
    }
    return render(request, "catalog/product_detail.html", context)
