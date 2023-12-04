from django.shortcuts import render
from Clientes.models import Cliente, Producto, Envio
from django.template import loader
from django.http import HttpResponse

# Create your views here.

# def cliente_nuevo(request):
#     cliente = Cliente(nombre='Marshall', nro_cuit='302545897', email='marshall@marshall', numero_cliente='01')
#     cliente.save()
#     template = loader.get_template('cliente.html')
#     doc = template.render({'nombre': cliente.nombre})
#     return HttpResponse(doc)

def cliente_nuevo(request):
    print("Mostrar request.post:")
    print(request.POST)
    
    if request.method == "POST":
        nuevo_cliente = Cliente(
            nombre = request.POST["nombre"],
            nro_cuit = request.POST["nro_cuit"],
            numero_cliente = request.POST["numero_cliente"],
            email = request.POST['email']
        )
        nuevo_cliente.save()
        return render(request, "index.html")
    
    return render(request, 'cliente_formulario.html')  

def producto(request):
    print("Mostrar request.post:")
    print(request.POST)
    
    if request.method == "POST":
        nuevo_producto = Producto(
            nombre = request.POST["nombre"],
            descripcion = request.POST["descripcion"],
            cantidad_en_stock = request.POST["cantidad_en_stock"]
        )
        nuevo_producto.save()
        return render(request, "index.html")
    
    return render(request, 'producto_formulario.html')  

def envio(request):
    print("Mostrar request.post:")
    print(request.POST)
    
    if request.method == "POST":
        nuevo_envio = Envio(
            direccion = request.POST["direccion"],
            localidad = request.POST["localidad"],
            telefono = request.POST["telefono"],
            fecha_envio = request.POST["fecha_envio"]
        )
        nuevo_envio.save()
        return render(request, "index.html")
    
    return render(request, 'envio_formulario.html')  