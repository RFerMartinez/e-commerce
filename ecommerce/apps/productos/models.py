from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre de Categoría')

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = 'categoriaProducto'
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
        ordering = ['nombre']

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=70, verbose_name='Nombre del Producto')
    imagen = models.ImageField(upload_to='imagenProducto/', blank=True, null=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']
