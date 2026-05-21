#Importa a função HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def sobre(rrquest):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def criar_perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse('Perfil criado')
    else:
            form = PerfilForm()
    return render(request, 'criar_perfil.html', ('form': form))