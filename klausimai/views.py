from django.shortcuts import render
from .forms import RegistracijosForma
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