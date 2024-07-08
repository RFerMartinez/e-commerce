from django.shortcuts import render

def home(request):
    
    ctx = {
        'texto_desde_def': 'asdasd',
        'num_desde_def': 21,
    }
    return render(request, 'home.html', ctx)