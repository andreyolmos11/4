from django.shortcuts import render, get_object_or_404
from .models import Cliente

def cliente_lista(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_lista.html', {'clientes': clientes})

def cliente_detalle(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'clientes/cliente_detalle.html', {'cliente': cliente})
