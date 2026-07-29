from django import forms
from .models import Asset


class AssetForm(forms.ModelForm):

    class Meta:
        model = Asset

        fields = [
            "category",
            "brand",
            "vendor",
            "asset_name",
            "model",
            "serial_number",
            "purchase_date",
            "purchase_cost",
            "warranty_expiry",
            "current_status",
            "remarks",
        ]

        widgets = {
            "purchase_date": forms.DateInput(attrs={"type": "date"}),
            "warranty_expiry": forms.DateInput(attrs={"type": "date"}),
            "remarks": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"