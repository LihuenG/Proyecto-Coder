from django.urls import path
from Clientes.views import cliente_nuevo, producto, envio, mostrar_productos, busqueda_en_bd

urlpatterns = [
    path('cliente_nuevo/', cliente_nuevo, name='cliente_nuevo'),
    path('producto/', producto, name='producto'),
    path('envio/', envio, name='envio'),
    path('mostrar_producto/', mostrar_productos, name='mostrar_producto'),
    path('busqueda_bd/', busqueda_en_bd, name='busqueda en bd'),

]
