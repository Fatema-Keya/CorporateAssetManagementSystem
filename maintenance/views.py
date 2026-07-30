from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import MaintenanceRecord
from .forms import MaintenanceForm
from django.contrib.auth.decorators import login_required
from utils.decorators import staff_required

@login_required
def maintenance_list(request):

    records = MaintenanceRecord.objects.select_related(
        "asset",
        "vendor",
        "created_by",
    )

    return render(
        request,
        "maintenance/maintenance_list.html",
        {
            "records": records
        },
    )

@login_required
@staff_required
def maintenance_create(request):

    if request.method == "POST":

        form = MaintenanceForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Maintenance record created successfully."
            )

            return redirect("maintenance_list")

    else:

        form = MaintenanceForm()

    return render(
        request,
        "maintenance/maintenance_form.html",
        {
            "form": form,
            "title": "Add Maintenance",
        },
    )

@login_required
@staff_required
def maintenance_update(request, pk):

    record = get_object_or_404(
        MaintenanceRecord,
        pk=pk
    )

    if request.method == "POST":

        form = MaintenanceForm(
            request.POST,
            instance=record
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Maintenance updated successfully."
            )

            return redirect("maintenance_list")

    else:

        form = MaintenanceForm(instance=record)

    return render(
        request,
        "maintenance/maintenance_form.html",
        {
            "form": form,
            "title": "Edit Maintenance",
        },
    )

@login_required
@staff_required
def maintenance_delete(request, pk):

    record = get_object_or_404(
        MaintenanceRecord,
        pk=pk
    )

    if request.method == "POST":

        record.delete()

        messages.success(
            request,
            "Maintenance deleted successfully."
        )

        return redirect("maintenance_list")

    return render(
        request,
        "maintenance/maintenance_confirm_delete.html",
        {
            "record": record
        },
    )
