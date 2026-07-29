from django.shortcuts import render
from assets.models import Asset, AssetAssignment
from employees.models import Employee
from maintenance.models import MaintenanceRecord
from requests_app.models import EmployeeRequest


def dashboard(request):

    context = {
        "total_assets": Asset.objects.count(),
        "available_assets": Asset.objects.filter(current_status="Available").count(),
        "assigned_assets": Asset.objects.filter(current_status="Assigned").count(),
        "maintenance_assets": Asset.objects.filter(current_status="Under Maintenance").count(),
        "lost_assets": Asset.objects.filter(current_status="Lost").count(),
        "total_employees": Employee.objects.count(),
        "pending_requests": EmployeeRequest.objects.filter(status="Pending").count(),
        "total_maintenance": MaintenanceRecord.objects.count(),
    }

    return render(request, "dashboard/dashboard.html", context)
