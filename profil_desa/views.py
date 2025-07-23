from django.shortcuts import render
from .models import PotensiDesa, GaleriFoto



def profil(request):
    semua_potensi = PotensiDesa.objects.all()
    semua_foto = GaleriFoto.objects.all()
    konteks = {
        'semua_potensi': semua_potensi,
        'semua_foto': semua_foto,
    }
    return render(request, 'profil_desa/profil.html', konteks)