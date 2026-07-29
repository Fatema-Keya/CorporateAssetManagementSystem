from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee

        fields = [
            "employee_code",
            "user",
            "department",
            "designation",
            "first_name",
            "last_name",
            "email",
            "phone",
            "joining_date",
            "status",
        ]

        widgets = {
            "joining_date": forms.DateInput(
                attrs={"type": "date"}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"