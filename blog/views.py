from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blog/index.html')

def ensaios(request):
    return render(request, 'blog/ensaios.html')

def sobre(request):
    return render(request, 'blog/sobre.html')

def contato(request):
    return render(request, 'blog/contato.html')

