from django.shortcuts import render, redirect, get_object_or_404
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
        klausimas_id = request.POST.get('klausimas_id')

        if klausimas_id:
            klausimas = get_object_or_404(Klausimas, id=klausimas_id)
            klausimas.atsakymas = request.POST.get('atsakymas')
            klausimas.atsake_vartotojas = request.user
            klausimas.save()
        else:
            tekstas = request.POST.get('tekstas')
            Klausimas.objects.create(tekstas=tekstas, uzduotas_vartotojas=request.user)

        return redirect('pagrindinis')

    neatsakyti = Klausimas.objects.filter(atsakymas__isnull=True)
    atsakyti = Klausimas.objects.exclude(atsakymas__isnull=True)

    return render(request, 'pagrindinis.html', {
        'neatsakyti': neatsakyti,
        'atsakyti': atsakyti
    })


def atsakyti(request, klausimo_id):
    klausimas = get_object_or_404(Klausimas, id=klausimo_id)

    if request.method == "POST":
        atsakymas = request.POST.get('atsakymas')
        klausimas.atsakymas = atsakymas
        klausimas.atsake_vartotojas = request.user
        klausimas.save()
        return redirect('pagrindinis')

    return render(request, 'atsakyti.html', {'klausimas': klausimas})