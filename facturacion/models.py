from django.db import models
from clientes.models import Cliente

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    productos = models.ManyToManyField('productos.Producto', through='DetalleFactura')

    def __str__(self):
        return f'Factura {self.id} - {self.cliente}'

class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey('productos.Producto', on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{self.factura} - {self.producto}'

    class Meta:
        unique_together = ('factura', 'producto')


