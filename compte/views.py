from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreerUtilisateur
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='acces')
def inscriptionPage(request):
    form = CreerUtilisateur()
    if request.method == 'POST':
        form = CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Compte Crée avec Succès pour '+user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'compte/inscription.html', context)


def singUp(request):
    if request.method == 'GET':
        return render(request, 'compte/signUp.html')


def accesPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('acceuil')
        else:
            messages.info(request, "Utilisateur ou mot de passe incorrecte ")

    return render(request, 'compte/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
