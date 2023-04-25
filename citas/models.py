from django.db import models
from clientes.models import Cliente

class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=100)
    confirmada = models.BooleanField(default=False)

    def __str__(self):
        return f"Cita de {self.cliente} el {self.fecha} a las {self.hora}"

