from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Client, Item, Purchase

admin.site.register(Client)
admin.site.register(Item)
admin.site.register(Purchase)

