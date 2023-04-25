from django.shortcuts import render, redirect, get_object_or_404
from .models import Factura, DetalleFactura
from .forms import FacturaForm

def factura_nueva(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            factura = form.save()
            return redirect('factura_editar', pk=factura.pk)
    else:
        form = FacturaForm()
    return render(request, 'facturacion/factura_editar.html', {'form': form})

def factura_editar(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    if request.method == 'POST':
        for detallefactura in factura.detallefactura_set.all():
            detallefactura.delete()
        for producto_id, cantidad in request.POST.items():
            if producto_id.isdigit() and int(cantidad) > 0:
                producto = get_object_or_404(producto, pk=producto_id)
                DetalleFactura.objects.create(factura=factura, producto=producto, cantidad=cantidad, precio=producto.precio)
        return redirect('factura_detalle', pk=factura.pk)
    else:
        productos = producto.objects.all()
        return render(request, 'facturacion/factura_editar.html', {'factura': factura, 'productos': productos})

def factura_detalle(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    return render(request, 'facturacion/factura_detalle.html', {'factura': factura})
