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


    def save(self, *args, **kwargs):

        if self.maintenance_status in ["Pending", "In Progress"]:
            self.asset.current_status = "Under Maintenance"

        elif self.maintenance_status == "Completed":
            self.asset.current_status = "Available"

        self.asset.save()

        super().save(*args, **kwargs)