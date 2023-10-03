
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products', include('produits.urls')),
    path('commandes', include('commandes.urls')),
    path('clients', include('clients.urls')),
    path('', include('compte.urls')),

]
