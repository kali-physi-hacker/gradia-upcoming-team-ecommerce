from django.urls import path 

from products.views import product_detail


urlpatterns = [
    path("products/<int:pk>/", product_detail, name="product_detail")
]