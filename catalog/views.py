from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Product, Category, Service, ServiceInquiry, Testimonial


def home(request):
    featured_products = Product.objects.filter(is_featured=True)[:6]
    services = Service.objects.all().order_by("order")
    categories = Category.objects.all()
    testimonials = Testimonial.objects.all()[:3]
    total_products = Product.objects.count()

    context = {
        "featured_products": featured_products,
        "services": services,
        "categories": categories,
        "testimonials": testimonials,
        "total_products": total_products,
    }
    return render(request, "catalog/home.html", context)


def product_list(request):
    categories = Category.objects.all()
    selected_category = request.GET.get("category", "").strip()
    selected_condition = request.GET.get("condition", "").strip()
    query = request.GET.get("q", "").strip()

    products = Product.objects.all()

    if selected_category:
        products = products.filter(category__slug=selected_category)

    if selected_condition:
        products = products.filter(condition=selected_condition)

    if query:
        products = products.filter(
            Q(name__icontains=query)
            | Q(tagline__icontains=query)
            | Q(description__icontains=query)
            | Q(key_features__icontains=query)
        )

    total_count = products.count()

    paginator = Paginator(products, 24)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    conditions = Product.CONDITION_CHOICES

    context = {
        "page_obj": page_obj,
        "products": page_obj.object_list,
        "categories": categories,
        "selected_category": selected_category,
        "selected_condition": selected_condition,
        "conditions": conditions,
        "query": query,
        "total_items": total_count,
    }
    return render(request, "catalog/product_list.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = (
        Product.objects.exclude(pk=pk)
        .filter(category=product.category)[:4]
    )

    context = {
        "product": product,
        "related_products": related_products,
        "features_list": product.get_features_list(),
    }
    return render(request, "catalog/product_detail.html", context)


def services_view(request):
    services = Service.objects.all().order_by("order")
    preselected_service = request.GET.get("service", "")

    if request.method == "POST":
        customer_name = request.POST.get("customer_name", "").strip()
        phone_or_whatsapp = request.POST.get("phone_or_whatsapp", "").strip()
        email = request.POST.get("email", "").strip()
        service_type = request.POST.get("service_type", "").strip()
        device_model = request.POST.get("device_model", "").strip()
        issue_or_specs = request.POST.get("issue_or_specs", "").strip()
        budget = request.POST.get("budget", "").strip()

        if customer_name and phone_or_whatsapp and issue_or_specs:
            inquiry = ServiceInquiry.objects.create(
                customer_name=customer_name,
                phone_or_whatsapp=phone_or_whatsapp,
                email=email,
                service_type=service_type or "General Inquiry",
                device_model=device_model,
                issue_or_specs=issue_or_specs,
                budget=budget,
            )
            messages.success(
                request,
                f"Thank you, {customer_name}! Your service request has been logged. Our lead technician will review your details and contact you via WhatsApp / phone shortly.",
            )
            return redirect("catalog:services")
        else:
            messages.error(request, "Please fill in all required fields (Name, Phone/WhatsApp, and Issue details).")

    context = {
        "services": services,
        "preselected_service": preselected_service,
    }
    return render(request, "catalog/services.html", context)


def about_view(request):
    testimonials = Testimonial.objects.all()
    context = {
        "testimonials": testimonials,
    }
    return render(request, "catalog/about.html", context)


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        contact = request.POST.get("contact", "").strip()
        message = request.POST.get("message", "").strip()
        subject = request.POST.get("subject", "General Inquiry").strip()

        if name and contact and message:
            ServiceInquiry.objects.create(
                customer_name=name,
                phone_or_whatsapp=contact,
                service_type=f"Contact Form: {subject}",
                issue_or_specs=message,
            )
            messages.success(
                request,
                f"Thank you, {name}! Your message has been received. Our team will reach out promptly.",
            )
            return redirect("catalog:contact")
        else:
            messages.error(request, "Please fill in your name, contact info, and message.")

    return render(request, "catalog/contact.html")
