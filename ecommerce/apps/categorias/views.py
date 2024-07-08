from django.shortcuts import render

def listar_categorias(request):
    data = {

    }
    return render(request, 'categorias/lista.html', data)
