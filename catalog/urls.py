from django.urls import path
from catalog import views

urlpatterns = [
    # Vehicles URLs
    path("vehicles/", views.VehicleList.as_view(), name="vehicle-list"),
    path("vehicles/<int:pk>/", views.VehicleDetail.as_view(), name="vehicle-detail"), 
    # Categorys URLs
    path("categorys/", views.CategoryList.as_view(), name="category-list"),
    path("categorys/<int:pk>/", views.CategoryDetail.as_view(), name="category-detail"),
]
