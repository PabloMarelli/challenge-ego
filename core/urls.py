"""core URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from core import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.ApiHome.as_view(), name="api-home"),
    path("catalog/", include('catalog.urls')),
    path("auth/", include('users.urls')),
]
