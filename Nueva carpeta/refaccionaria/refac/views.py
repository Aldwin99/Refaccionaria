from django.shortcuts import render, redirect
from pyexpat.errors import messages
from .models import Refaccion
from .forms import AddRefaccionForm
from django.contrib import messages
# Create your views here.
def ventas_view(request):
    refacciones = Refaccion.objects.all()
    context ={
        'refacciones': refacciones

    }

    return render(request, 'ventas.html',context)

def refacciones_view(request):
    refacciones = Refaccion.objects.all()
    form_refac =AddRefaccionForm
    context ={
       'refacciones': refacciones,
        'form_personal': form_refac,
    }
    
    return render(request, 'productos.html', context)



def add_refacciones_view(request):
    if request.POST:
        form = AddRefaccionForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                    messages(request, "Error al guardar refacción")
                    return redirect('Refacciones')
    return redirect('Refacciones')
""""
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session["carrito"]
        if not carrito: 
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else: 
            self.carrito = carrito

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "acumulado": producto.precio,
                "cantidad": 1,
            } 
        else: 
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precio
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id not in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar (self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
    	    self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
"""








