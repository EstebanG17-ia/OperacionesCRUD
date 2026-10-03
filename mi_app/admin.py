from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stock', 'fecha_registro')
    search_fields = ('nombre',)
    list_filter = ('fecha_registro',)