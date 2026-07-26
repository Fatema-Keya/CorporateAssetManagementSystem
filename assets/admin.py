from django.contrib import admin
from .models import AssetCategory, Brand, Vendor, Asset, AssetAssignment

admin.site.register(AssetCategory)
admin.site.register(Brand)
admin.site.register(Vendor)

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = (
        'asset_code',
        'asset_name',
        'category',
        'brand',
        'current_status',
    )

    search_fields = (
        'asset_code',
        'asset_name',
        'serial_number',
    )

    list_filter = (
        'category',
        'brand',
        'current_status',
    )

@admin.register(AssetAssignment)
class AssetAssignmentAdmin(admin.ModelAdmin):
    list_display = (
        'asset',
        'employee',
        'assigned_date',
        'status',
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'asset__asset_code',
        'employee__employee_code',
    )
