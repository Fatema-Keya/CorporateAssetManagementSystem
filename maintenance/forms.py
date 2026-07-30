from django import forms
from .models import MaintenanceRecord


class MaintenanceForm(forms.ModelForm):

    class Meta:
        model = MaintenanceRecord

        fields = [
            "asset",
            "vendor",
            "issue_description",
            "maintenance_cost",
            "start_date",
            "end_date",
            "maintenance_status",
            "remarks",
            "created_by",
        ]

        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
            "issue_description": forms.Textarea(attrs={"rows": 3}),
            "remarks": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"