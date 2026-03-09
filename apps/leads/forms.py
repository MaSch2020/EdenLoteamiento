from django import forms

from apps.lots.models import Lot
from apps.leads.models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ["full_name", "phone", "email", "lot", "message"]
        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Tu nombre y apellido",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Tu número de contacto",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Tu correo (opcional)",
                }
            ),
            "lot": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Cuéntanos qué lote o información te interesa",
                    "rows": 4,
                }
            ),
        }
        labels = {
            "full_name": "Nombre completo",
            "phone": "Teléfono",
            "email": "Correo electrónico",
            "lot": "Lote de interés",
            "message": "Mensaje",
        }

    def __init__(self, *args, **kwargs):
        project = kwargs.pop("project", None)
        super().__init__(*args, **kwargs)

        queryset = Lot.objects.filter(status=Lot.STATUS_AVAILABLE).select_related("project")
        if project is not None:
            queryset = queryset.filter(project=project)

        self.fields["lot"].queryset = queryset
        self.fields["lot"].required = False
        self.fields["lot"].empty_label = "Selecciona un lote disponible"
        self.fields["email"].required = False
        self.fields["message"].required = False