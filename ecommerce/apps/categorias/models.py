from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre de Categoría')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = 'categoriaProducto'
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
        ordering = ['nombre']
