from django.db import models
from clients.models import Clients
from produits.models import Produits


# Create your models here.
class Commandes(models.Model):
    STATUS=(('en instance', 'en instance'),
            ('nom Livré', 'nom Livré'),
            ('Livré', 'Livré'))


    client=models.ForeignKey(Clients,null=True,on_delete=models.SET_NULL)
    produit=models.ForeignKey(Produits,null=True,on_delete=models.SET_NULL)
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    date_creation=models.DateTimeField(auto_now_add=True,null=True)
