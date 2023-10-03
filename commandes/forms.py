from django.forms import ModelForm
from .models import Commandes

class CommandesForm(ModelForm):
    class Meta:
        model=Commandes
        fields='__all__'