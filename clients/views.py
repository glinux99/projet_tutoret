from django.shortcuts import render
#from django.http import HttpResponse
from .models import Clients
from commandes.filters import CommandesFiltre
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='acces')
def list_clients(request,pk):
    clients=Clients.objects.get(id=pk)
    commandes=clients.commandes_set.all()
    commandes_total=commandes.count()
    myFilter=CommandesFiltre(request.GET,queryset=commandes)
    commandes=myFilter.qs


    context={'clients':clients, 'commandes':commandes, 'commandes_total':commandes_total,'myFilter':myFilter}
    return render(request,'clients/list_client.html',context)
