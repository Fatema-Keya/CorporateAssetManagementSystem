from django.contrib import admin
from .models import Department, Designation, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'department_code',
        'department_name',
        'status',
    )

    search_fields = (
        'department_code',
        'department_name',
    )

    list_filter = (
        'status',
    )


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = (
        'designation_name',
        'status',
    )

    search_fields = (
        'designation_name',
    )

    list_filter = (
        'status',
    )

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'employee_code',
        'first_name',
        'last_name',
        'department',
        'designation',
        'status',
    )

    search_fields = (
        'employee_code',
        'first_name',
        'last_name',
        'email',
    )

    list_filter = (
        'department',
        'designation',
        'status',
    )