from django import forms
from .models import EmployeeRequest


class EmployeeRequestForm(forms.ModelForm):

    class Meta:
        model = EmployeeRequest

        fields = [
            "employee",
            "request_type",
            "asset_category",
            "asset",
            "description",
            "status",
            "approved_by",
        ]

        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"