from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def employee_list(request):
    query = request.GET.get("q")

    employees = Employee.objects.select_related(
        "department",
        "designation",
        "user"
    )

    if query:
        employees = employees.filter(
            employee_code__icontains=query
        ) | employees.filter(
            first_name__icontains=query
        ) | employees.filter(
            last_name__icontains=query
        )

    context = {
        "employees": employees,
        "query": query,
    }
    paginator = Paginator(employees, 10)

    page_number = request.GET.get("page")

    employees = paginator.get_page(page_number)
    
    return render(
        request,
        "employees/employee_list.html",
        context,
    )

@login_required
def employee_create(request):

    if request.method == "POST":

        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Employee created successfully."
            )

            return redirect("employee_list")

    else:
        form = EmployeeForm()

    return render(
        request,
        "employees/employee_form.html",
        {
            "form": form,
            "title": "Add Employee",
        },
    )

@login_required
def employee_update(request, pk):

    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":

        form = EmployeeForm(
            request.POST,
            instance=employee
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Employee updated successfully."
            )

            return redirect("employee_list")

    else:
        form = EmployeeForm(instance=employee)

    return render(
        request,
        "employees/employee_form.html",
        {
            "form": form,
            "title": "Edit Employee",
        },
    )

@login_required
def employee_delete(request, pk):

    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        employee.delete()

        messages.success(
            request,
            "Employee deleted successfully."
        )

        return redirect("employee_list")

    return render(
        request,
        "employees/employee_confirm_delete.html",
        {
            "employee": employee,
        },
    )

