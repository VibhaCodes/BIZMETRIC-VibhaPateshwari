from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # DRF APIs
    path("api/", include("user.urls")),
    path("api/", include("customer.urls")),
]