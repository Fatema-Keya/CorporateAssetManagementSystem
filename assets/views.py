from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Asset
from .forms import AssetForm


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


def asset_create(request):

    if request.method == "POST":

        form = AssetForm(request.POST)

        if form.is_valid():

            form.save()

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


def asset_update(request, pk):

    asset = get_object_or_404(Asset, pk=pk)

    if request.method == "POST":

        form = AssetForm(
            request.POST,
            instance=asset
        )

        if form.is_valid():

            form.save()

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


def asset_delete(request, pk):

    asset = get_object_or_404(Asset, pk=pk)

    if request.method == "POST":

        asset.delete()

        return redirect("asset_list")

    return render(
        request,
        "assets/asset_confirm_delete.html",
        {
            "asset": asset
        }
    )