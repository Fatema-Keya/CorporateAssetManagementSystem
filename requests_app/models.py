from django.db import models
from django.conf import settings
from employees.models import Employee
from assets.models import Asset, AssetCategory


class EmployeeRequest(models.Model):

    REQUEST_TYPES = (
        ("New Asset", "New Asset"),
        ("Replacement", "Replacement"),
        ("Damage Report", "Damage Report"),
    )

    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
        ("Completed", "Completed"),
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    request_type = models.CharField(
        max_length=30,
        choices=REQUEST_TYPES
    )

    asset_category = models.ForeignKey(
        AssetCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    asset = models.ForeignKey(
        Asset,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    approved_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.employee.employee_code} - {self.request_type}"
