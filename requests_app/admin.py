from django.contrib import admin
from .models import EmployeeRequest


@admin.register(EmployeeRequest)
class EmployeeRequestAdmin(admin.ModelAdmin):

    list_display = (
        "employee",
        "request_type",
        "status",
        "approved_by",
        "created_at",
    )

    list_filter = (
        "status",
        "request_type",
    )

    search_fields = (
        "employee__employee_code",
        "description",
    )