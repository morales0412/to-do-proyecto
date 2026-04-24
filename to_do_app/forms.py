from django import forms

from to_do_app.models import Tarea


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ["titulo", "descripcion", "fecha_vencimiento"]
        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "placeholder": "Ej. Estudiar Django",
                    "autocomplete": "off",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Describe la tarea con un poco de contexto.",
                }
            ),
            "fecha_vencimiento": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            ),
        }
