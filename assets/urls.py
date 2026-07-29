from django.urls import path

from .views import (
    asset_list,
    asset_create,
    asset_update,
    asset_delete,
)

urlpatterns = [
    path("", asset_list, name="asset_list"),
    path("add/", asset_create, name="asset_create"),
    path("edit/<int:pk>/", asset_update, name="asset_update"),
    path("delete/<int:pk>/", asset_delete, name="asset_delete"),
]