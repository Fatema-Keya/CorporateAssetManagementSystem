from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Dashboard
    path("", include("dashboard.urls")),

    # Employees
    path("employees/", include("employees.urls")),

    # Assets
    path("assets/", include("assets.urls")),

    # Maintenance
    path("maintenance/", include("maintenance.urls")),

    # Employee Requests
    path("requests/", include("requests_app.urls")),

    # Reports
    path("reports/", include("reports.urls")),
]