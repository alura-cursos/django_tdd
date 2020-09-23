from django.shortcuts import render
from animais.models import Animal

def index(request):
    context = {'caracteristicas' : Animal.objects.all()}
    return render(request, 'index.html', context)