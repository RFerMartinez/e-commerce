from django.db import models

from datetime import date

class Tipo(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Tipo de empleado')

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = 'tipoEmpleado'
        verbose_name = 'TipoEmpleado'
        verbose_name_plural = 'TiposEmpleados'
        ordering = ['id']

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre de Categoría')

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = 'categoriaEmpleado'
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
        ordering = ['nombre']

class Empleado(models.Model):
    categoria = models.ManyToManyField(Categoria)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=70, verbose_name='Nombres')
    apellido = models.CharField(max_length=70, verbose_name='Apellidos')
    dni = models.CharField(max_length=8, verbose_name='D.N.I.', unique=True)
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    cantidad_hijos = models.PositiveIntegerField(null=True, verbose_name='Cantidad de Hijos')
    sexo = models.CharField(max_length=10, null=True) # Tal vez se pueda hacer otra tabla, llamando con ForeignKey

    fecha_registro = models.DateField(auto_now_add=True, verbose_name='Fecha de registro') # blank=True
    fecha_actualizacion = models.DateField(auto_now=True)
    salario = models.DecimalField(default=0.00, max_digits=9, decimal_places=2) # decimal_places=2. 'dos lugares despues de la coma'
    estado = models.BooleanField(default=True)

    imagen_perfil = models.ImageField(null=True, blank=True, upload_to='imagenPerfil/')
    curriculum_vitae = models.ImageField(null=True, blank=True, upload_to='curriculumVitae/')

    @property
    def edad(self):
        today = date.today() # date.today() obtiene la fecha actual del sistema. Almacena el año, mes y dia actual
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
    
    def __str__(sefl):
        return f"{sefl.apellido}, {sefl.nombre} - {sefl.edad} años."
    
    class Meta:
        db_table = 'empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']






