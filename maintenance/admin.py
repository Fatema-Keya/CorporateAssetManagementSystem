from django.contrib import admin
from .models import MaintenanceRecord


@admin.register(MaintenanceRecord)
class MaintenanceRecordAdmin(admin.ModelAdmin):

    list_display = (
        "asset",
        "vendor",
        "maintenance_status",
        "start_date",
        "end_date",
        "maintenance_cost",
    )

    search_fields = (
        "asset__asset_code",
        "vendor__vendor_name",
    )

    list_filter = (
        "maintenance_status",
    )