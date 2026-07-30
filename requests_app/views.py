from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import EmployeeRequest
from .forms import EmployeeRequestForm
from django.contrib.auth.decorators import login_required

@login_required
def request_list(request):

    requests = EmployeeRequest.objects.select_related(
        "employee",
        "asset",
        "asset_category",
        "approved_by",
    )

    return render(
        request,
        "requests_app/request_list.html",
        {
            "requests": requests,
        },
    )

@login_required
def request_create(request):

    if request.method == "POST":

        form = EmployeeRequestForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Request submitted successfully."
            )

            return redirect("request_list")

    else:

        form = EmployeeRequestForm()

    return render(
        request,
        "requests_app/request_form.html",
        {
            "form": form,
            "title": "Create Request",
        },
    )

@login_required
def request_update(request, pk):

    employee_request = get_object_or_404(
        EmployeeRequest,
        pk=pk
    )

    if request.method == "POST":

        form = EmployeeRequestForm(
            request.POST,
            instance=employee_request
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Request updated successfully."
            )

            return redirect("request_list")

    else:

        form = EmployeeRequestForm(instance=employee_request)

    return render(
        request,
        "requests_app/request_form.html",
        {
            "form": form,
            "title": "Edit Request",
        },
    )

@login_required
def request_delete(request, pk):

    employee_request = get_object_or_404(
        EmployeeRequest,
        pk=pk
    )

    if request.method == "POST":

        employee_request.delete()

        messages.success(
            request,
            "Request deleted successfully."
        )

        return redirect("request_list")

    return render(
        request,
        "requests_app/request_confirm_delete.html",
        {
            "request_obj": employee_request,
        },
    )

@login_required
def request_approve(request, pk):

    employee_request = get_object_or_404(
        EmployeeRequest,
        pk=pk
    )

    employee_request.status = "Approved"
    employee_request.save()

    messages.success(
        request,
        "Request approved successfully."
    )

    return redirect("request_list")

@login_required
def request_reject(request, pk):

    employee_request = get_object_or_404(
        EmployeeRequest,
        pk=pk
    )

    employee_request.status = "Rejected"
    employee_request.save()

    messages.success(
        request,
        "Request rejected successfully."
    )

    return redirect("request_list")
