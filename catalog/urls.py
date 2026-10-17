from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.product_list, name="product_list"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("services/", views.services_view, name="services"),
    path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),
]
