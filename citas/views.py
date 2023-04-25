from django.shortcuts import render, get_object_or_404
from .models import Cita

def lista_citas(request):
    citas = Cita.objects.all()
    return render(request, 'citas/lista_citas.html', {'citas': citas})

def detalle_cita(request, cita_id):
    cita = get_object_or_404(Cita, pk=cita_id)
    return render(request, 'citas/detalle_cita.html', {'cita': cita})

