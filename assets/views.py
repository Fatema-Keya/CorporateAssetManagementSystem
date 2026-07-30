from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages

from .models import Asset, AssetAssignment
from .forms import AssetForm, AssetAssignmentForm
from django.contrib.auth.decorators import login_required
from utils.decorators import staff_required


# ==========================
# Asset CRUD
# ==========================
@login_required
@staff_required
def asset_list(request):

    query = request.GET.get("q")

    assets = Asset.objects.all()

    if query:
        assets = assets.filter(
            Q(asset_name__icontains=query) |
            Q(asset_code__icontains=query) |
            Q(serial_number__icontains=query)
        )

    return render(
        request,
        "assets/asset_list.html",
        {
            "assets": assets,
            "query": query
        }
    )

@login_required
@staff_required
def asset_create(request):

    if request.method == "POST":

        form = AssetForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Asset created successfully.")
            return redirect("asset_list")

    else:
        form = AssetForm()

    return render(
        request,
        "assets/asset_form.html",
        {
            "form": form
        }
    )

@login_required
@staff_required
def asset_update(request, pk):

    asset = get_object_or_404(Asset, pk=pk)

    if request.method == "POST":

        form = AssetForm(
            request.POST,
            instance=asset
        )

        if form.is_valid():
            form.save()
            messages.success(request, "Asset updated successfully.")
            return redirect("asset_list")

    else:
        form = AssetForm(instance=asset)

    return render(
        request,
        "assets/asset_form.html",
        {
            "form": form
        }
    )

@login_required
@staff_required
def asset_delete(request, pk):

    asset = get_object_or_404(Asset, pk=pk)

    if request.method == "POST":
        asset.delete()
        messages.success(request, "Asset deleted successfully.")
        return redirect("asset_list")

    return render(
        request,
        "assets/asset_confirm_delete.html",
        {
            "asset": asset
        }
    )


# ==========================
# Asset Assignment
# ==========================
@login_required
@staff_required
def assignment_list(request):

    assignments = AssetAssignment.objects.select_related(
        "asset",
        "employee",
        "assigned_by"
    )

    return render(
        request,
        "assets/assignment_list.html",
        {
            "assignments": assignments
        }
    )

@login_required
@staff_required
def assignment_create(request):

    if request.method == "POST":

        form = AssetAssignmentForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Asset assigned successfully."
            )

            return redirect("assignment_list")

    else:
        form = AssetAssignmentForm()

    return render(
        request,
        "assets/assignment_form.html",
        {
            "form": form,
            "title": "Assign Asset",
        }
    )

@login_required
@staff_required
def assignment_return(request, pk):

    assignment = get_object_or_404(
        AssetAssignment,
        pk=pk
    )

    assignment.status = "Returned"

    assignment.asset.current_status = "Available"

    assignment.asset.save()

    assignment.save()

    messages.success(
        request,
        "Asset returned successfully."
    )

    return redirect("assignment_list")