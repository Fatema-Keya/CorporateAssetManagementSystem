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
    )

    list_filter = (
        "maintenance_status",
    )

    search_fields = (
        "asset__asset_code",
    )