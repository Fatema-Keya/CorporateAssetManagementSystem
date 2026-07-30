from django.urls import path

from .views import (
    request_list,
    request_create,
    request_update,
    request_delete,
    request_approve,
    request_reject,
)

urlpatterns = [
    path(
        "",
        request_list,
        name="request_list",
    ),

    path(
        "add/",
        request_create,
        name="request_create",
    ),

    path(
        "edit/<int:pk>/",
        request_update,
        name="request_update",
    ),

    path(
        "delete/<int:pk>/",
        request_delete,
        name="request_delete",
    ),

    path(
        "approve/<int:pk>/",
        request_approve,
        name="request_approve",
    ),

    path(
        "reject/<int:pk>/",
        request_reject,
        name="request_reject",
    ),
]