import django_filters
from .models import Commandes

class CommandesFiltre(django_filters.FilterSet):
    class Meta:
        model=Commandes
        fields='__all__'
        exclude=['client','date_creation']