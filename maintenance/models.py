from django.db import models
from django.conf import settings
from assets.models import Asset, Vendor


class MaintenanceRecord(models.Model):

    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    )

    asset = models.ForeignKey(
        Asset,
        on_delete=models.PROTECT
    )

    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.PROTECT
    )

    issue_description = models.TextField()

    maintenance_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    start_date = models.DateField()

    end_date = models.DateField(
        null=True,
        blank=True
    )

    maintenance_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    remarks = models.TextField(
        blank=True
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.asset.asset_code} - {self.maintenance_status}"
