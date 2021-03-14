from django.urls import path 
from products.views import product_list 


urlpatterns = [
    path("products/", product_list, name="product_list"),
    path("products/<int:pk>/", product_detail, name="product_detail")
]