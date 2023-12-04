from django.contrib import admin

# Register your models here.

from Clientes.models import Cliente, Envio, Producto

admin.site.register(Cliente)
admin.site.register(Envio)
admin.site.register(Producto)