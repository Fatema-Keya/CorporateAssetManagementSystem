from django.urls import path

from .views import reports_dashboard
from .views import reports_dashboard, export_assets_csv

urlpatterns = [
    path("",reports_dashboard,name="reports_dashboard",),
    path("export/assets/",export_assets_csv,name="export_assets_csv",),
]