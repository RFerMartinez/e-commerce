from django.urls import path

from . import views

app_name = 'categorias'

urlpatterns = [
    path('lista/', views.listar_categorias, name='listar_categorias')
]