from django.contrib import admin
from .models import Produits
from .models import Tag

# Register your models here.
admin.site.register(Produits)
admin.site.register(Tag)