from django.contrib import admin
from django.urls import path

from products.views import test_view

urlpatterns = [path("admin/", admin.site.urls), path("home/", test_view)]
