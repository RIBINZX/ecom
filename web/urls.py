# Create web/urls.py and paste the following
from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("shop/", views.shop, name="shop"),
    path("product-details/<str:id>/", views.product_details, name="product-details"),
    path("category-shop/<str:id>/", views.category_shop, name="category-shop"),
]