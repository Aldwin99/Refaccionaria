from django import forms
from refac.models import Refaccion


class AddRefaccionForm(forms.ModelForm):
    class Meta:
        models = Refaccion
        fields = ('nombre', 'description', 'modelo', 'precio', 'cantidad')
        labels = {
            'nombre': 'Nombre de la refaccion',
            'description': 'Descripción',
            'modelo': 'Modelo de la refaccion',
            'precio': 'precio de la refaccion',
            'cantidad': 'cantiadad de esta refaccion'

        } 