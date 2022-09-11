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