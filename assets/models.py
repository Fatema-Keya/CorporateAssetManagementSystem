from django.db import models
from django.conf import settings
from employees.models import Employee
from django.core.exceptions import ValidationError


class AssetCategory(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.brand_name


class Vendor(models.Model):

    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    vendor_name = models.CharField(max_length=150)
    contact_person = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Active'
    )

    def __str__(self):
        return self.vendor_name


class Asset(models.Model):

    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('Assigned', 'Assigned'),
        ('Under Maintenance', 'Under Maintenance'),
        ('Damaged', 'Damaged'),
        ('Lost', 'Lost'),
        ('Retired', 'Retired'),
    )

    asset_code = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )

    category = models.ForeignKey(
        AssetCategory,
        on_delete=models.PROTECT
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT
    )

    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.PROTECT
    )

    asset_name = models.CharField(max_length=100)

    model = models.CharField(max_length=100)

    serial_number = models.CharField(
        max_length=100,
        unique=True
    )

    purchase_date = models.DateField()

    purchase_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    warranty_expiry = models.DateField()

    current_status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Available'
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.asset_code} - {self.asset_name}"

    def save(self, *args, **kwargs):
        if not self.asset_code:
            last_asset = Asset.objects.order_by('id').last()

            if last_asset:
                last_id = last_asset.id + 1
            else:
                last_id = 1

            self.asset_code = f"AST{last_id:04d}"

        super().save(*args, **kwargs)


class AssetAssignment(models.Model):

    STATUS_CHOICES = (
        ('Assigned', 'Assigned'),
        ('Returned', 'Returned'),
    )

    asset = models.ForeignKey(
        Asset,
        on_delete=models.PROTECT
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT
    )

    assigned_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )

    assigned_date = models.DateField()

    expected_return_date = models.DateField(
        null=True,
        blank=True
    )

    returned_date = models.DateField(
        null=True,
        blank=True
    )

    return_condition = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Assigned'
    )

    remarks = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.asset.asset_code} → {self.employee.employee_code}"

    def clean(self):

    # Asset must be Available
        if self.asset.current_status != "Available":
            raise ValidationError(
                "Only Available assets can be assigned."
            )

    # Employee cannot have more than one Laptop
        if self.asset.category.category_name.lower() == "laptop":

            already_has_laptop = AssetAssignment.objects.filter(
                employee=self.employee,
                status="Assigned",
                asset__category__category_name__iexact="Laptop"
            ).exclude(pk=self.pk)

        if already_has_laptop.exists():
            raise ValidationError(
                "This employee already has a Laptop assigned."
            )
    def save(self, *args, **kwargs):

        self.full_clean()

        self.asset.current_status = "Assigned"
        self.asset.save()

        super().save(*args, **kwargs)

class AssetAuditLog(models.Model):

    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE
    )

    action = models.CharField(max_length=100)

    performed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asset.asset_code} - {self.action}"