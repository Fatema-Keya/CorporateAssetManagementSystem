from django.shortcuts import render

import csv
from django.http import HttpResponse
from assets.models import Asset
from employees.models import Employee
from maintenance.models import MaintenanceRecord
from requests_app.models import EmployeeRequest
from django.contrib.auth.decorators import login_required
from utils.decorators import admin_required

@login_required
@admin_required
def reports_dashboard(request):

    context = {

        "total_assets": Asset.objects.count(),

        "available_assets": Asset.objects.filter(
            current_status="Available"
        ).count(),

        "assigned_assets": Asset.objects.filter(
            current_status="Assigned"
        ).count(),

        "maintenance_assets": Asset.objects.filter(
            current_status="Under Maintenance"
        ).count(),

        "lost_assets": Asset.objects.filter(
            current_status="Lost"
        ).count(),

        "total_employees": Employee.objects.count(),

        "active_employees": Employee.objects.filter(
            status="Active"
        ).count(),

        "inactive_employees": Employee.objects.filter(
            status="Inactive"
        ).count(),

        "total_maintenance": MaintenanceRecord.objects.count(),

        "pending_maintenance": MaintenanceRecord.objects.filter(
            maintenance_status="Pending"
        ).count(),

        "completed_maintenance": MaintenanceRecord.objects.filter(
            maintenance_status="Completed"
        ).count(),

        "pending_requests": EmployeeRequest.objects.filter(
            status="Pending"
        ).count(),

        "approved_requests": EmployeeRequest.objects.filter(
            status="Approved"
        ).count(),

        "rejected_requests": EmployeeRequest.objects.filter(
            status="Rejected"
        ).count(),
    }

    return render(
        request,
        "reports/report_dashboard.html",
        context,
    )

@login_required
@admin_required
def export_assets_csv(request):

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="assets_report.csv"'

    writer = csv.writer(response)

    writer.writerow([
        "Asset Code",
        "Asset Name",
        "Category",
        "Brand",
        "Status",
        "Purchase Cost",
    ])

    assets = Asset.objects.all()

    for asset in assets:

        writer.writerow([
            asset.asset_code,
            asset.asset_name,
            asset.category,
            asset.brand,
            asset.current_status,
            asset.purchase_cost,
        ])

    return response
