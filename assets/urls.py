from django.urls import path

from .views import (
    asset_list,
    asset_create,
    asset_update,
    asset_delete,
    assignment_list,
    assignment_create,
    assignment_return,
)

urlpatterns = [
    path("", asset_list, name="asset_list"),
    path("add/", asset_create, name="asset_create"),
    path("edit/<int:pk>/", asset_update, name="asset_update"),
    path("delete/<int:pk>/", asset_delete, name="asset_delete"),
    path("assignments/",assignment_list,name="assignment_list"),
    path("assignments/add/",assignment_create,name="assignment_create",),
    path("assignments/return/<int:pk>/",assignment_return,name="assignment_return",),
]