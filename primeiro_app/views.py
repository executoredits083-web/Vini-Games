#Importa a função HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('Ola, este é o meu primeiro projeto Django')