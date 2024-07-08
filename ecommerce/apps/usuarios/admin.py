from django.contrib import admin

from .models import Categoria, Empleado, Tipo

admin.site.register(Empleado)

admin.site.register(Categoria)

admin.site.register(Tipo)
