from django.shortcuts import render, redirect
from .forms import RegistracijosForma
from .models import Klausimas
# Create your views here.

def registracija(request):
    if request.method == 'POST':
        forma = RegistracijosForma(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect('pagrindinis')
    else:
        forma = RegistracijosForma()
    return render(request, 'registration/register.html', {'forma': forma})


def pagrindinis(request):
    if request.method == 'POST':
        tekstas = request.POST.get('tekstas')
        Klausimas.objects.create(tekstas=tekstas, uzduotas_vartotojas=request.user)
        return redirect('pagrindinis')

    neatsakyti = Klausimas.objects.filter(atsakymas__isnull=True)
    atsakyti = Klausimas.objects.exclude(atsakymas__isnull=True)

    return render(request, 'pagrindinis.html', {
        'neatsakyti': neatsakyti,
        'atsakyti': atsakyti
    })