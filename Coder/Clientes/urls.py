from django.urls import path
from Clientes.views import cliente_nuevo, producto, envio

urlpatterns = [
    path('cliente_nuevo/', cliente_nuevo, name='cliente_nuevo'),
    path('producto/', producto, name='producto'),
    path('envio/', envio, name='envio')
    
]
