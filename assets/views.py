from django.shortcuts import render
from .models import Asset


def asset_list(request):
    assets = Asset.objects.select_related(
        "category",
        "brand",
        "vendor"
    )

    context = {
        "assets": assets
    }

    return render(
        request,
        "assets/asset_list.html",
        context
    )
