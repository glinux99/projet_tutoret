from django.urls import path
from . import views

urlpatterns = [
    # path('signUp', views.inscriptionPage, name='singup'),
    path('signUp', views.singUp, name='singup'),
    path('login', views.accesPage, name='login'),
    path('quitter', views.logoutUser, name='quitter'),

]
