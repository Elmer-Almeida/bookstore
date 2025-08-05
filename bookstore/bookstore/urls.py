from django.contrib import admin
from django.urls import path, include

from .views import LandingPage

urlpatterns = [
    path("admin/", admin.site.urls),
    path('books/', include('store.urls')),

    path("", LandingPage.as_view(), name="landing"),
]
