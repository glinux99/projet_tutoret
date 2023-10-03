from django.shortcuts import render, HttpResponse
#from django.http import
from commandes.models import Commandes
from commandes.models import Clients
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='acces')
def home(request):
    commandes=Commandes.objects.all()
    clients=Clients.objects.all()
    context={'commandes':commandes,'clients':clients}
    return render(request,'produits/acceuil.html', context)
