from django.urls import path

from .views import (
    maintenance_list,
    maintenance_create,
    maintenance_update,
    maintenance_delete,
)

urlpatterns = [
    path(
        "",
        maintenance_list,
        name="maintenance_list",
    ),

    path(
        "add/",
        maintenance_create,
        name="maintenance_create",
    ),

    path(
        "edit/<int:pk>/",
        maintenance_update,
        name="maintenance_update",
    ),

    path(
        "delete/<int:pk>/",
        maintenance_delete,
        name="maintenance_delete",
    ),
]