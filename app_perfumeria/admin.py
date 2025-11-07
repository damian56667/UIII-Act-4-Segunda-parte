from django.contrib import admin
from .models import Empleado, Producto, Cliente

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'puesto', 'email', 'activo')
    search_fields = ('nombre', 'apellido', 'puesto')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stock', 'categoria', 'activo', 'sku')
    search_fields = ('nombre', 'categoria', 'sku')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','apellido','email','ciudad','activo')
    search_fields = ('nombre','apellido','email')
