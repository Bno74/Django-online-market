from django.contrib import admin

from .models import Catagory, Item


admin.site.register(Catagory)
admin.site.register(Item)

class Meta:
        verbose_name_plural = 'Categories'

