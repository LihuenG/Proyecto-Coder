from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    nro_cuit = models.IntegerField()
    email = models.EmailField()
    numero_cliente = models.IntegerField()
    
    def __str__(self):
        return self.nombre + ' CUIT: ' + str(self.nro_cuit)
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    cantidad_en_stock = models.IntegerField()

class Envio(models.Model):
    #cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='Envios')
    #producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='Envios')
    direccion = models.CharField(max_length=70)
    localidad = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fecha_envio = models.DateField()
    
    