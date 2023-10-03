from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CommandesForm
from .models import Commandes
from django.contrib.auth.decorators import login_required





# Create your views here.
@login_required(login_url='acces')
def list_commandes(request):
    return render(request,'commandes/list_commandes.html')

def ajouter_commande(request):
    form=CommandesForm()
    if request.method=='POST':
        form=CommandesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request,'commandes/ajouter_commandes.html',context)

def modifier_commande(request,pk):
    commandes=Commandes.objects.get(id=pk)
    form=CommandesForm(instance=commandes)

    if request.method=='POST':
        form=CommandesForm(request.POST,instance=commandes)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request,'commandes/ajouter_commandes.html',context)


def supprimer_commandes(request,pk):
    commandes = Commandes.objects.get(id=pk)
    if request.method == 'POST':
        commandes.delete()
        return redirect('/')
    context = {'item': commandes}


    return render(request,'commandes/supprimer_commandes.html', context)

