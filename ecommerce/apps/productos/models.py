from django.db import models

from ..categorias.models import Categoria

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=70, verbose_name='Nombre del Producto')
    imagen = models.ImageField(upload_to='imagenProducto/', blank=True, null=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']

