from django.db import models
from django.utils.translation import gettext as _

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    imagen = models.ImageField(upload_to='productos_images', null=True, blank=True)

    def __str__(self):
        return self.nombre

    def precio_en_pesos(self):
        return _("${:.2f} COP").format(self.precio * 3500)  # 1 USD = 3500 COP
    precio_en_pesos.short_description = 'Precio en pesos colombianos'


