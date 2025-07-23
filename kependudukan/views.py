from django.shortcuts import render, redirect, get_object_or_404
from .models import Warga
from .forms import WargaForm
# Create your views here.

def daftar_warga(request):
    semua_warga = Warga.objects.all()
    print(semua_warga)

    konteks = {
        'semua_warga': semua_warga
    }

    return render(request, 'kependudukan/daftar_warga.html', konteks)


def tambah_warga(request):
    if request.method == 'POST':
        form = WargaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_warga')
    else:
        form = WargaForm()
    
    konteks = {
        'form': form
    }

    return render(request, 'kependudukan/form_warga.html', konteks)

# View BARU untuk mengubah warga
def ubah_warga(request, warga_id):
    # Ambil objek warga berdasarkan ID, atau tampilkan 404 jika tidak ada
    warga = get_object_or_404(Warga, id=warga_id)

    if request.method == 'POST':
        # Proses data yang dikirim dari form
        form = WargaForm(request.POST, instance=warga)
        if form.is_valid():
            form.save() # Simpan perubahan
            return redirect('daftar_warga')
    else:
        # Tampilkan form yang sudah terisi dengan data warga yang ada
        form = WargaForm(instance=warga)

    konteks = {
        'form': form,
    }
    return render(request, 'kependudukan/form_warga.html', konteks)

# View untuk menghapus warga
def hapus_warga(request, warga_id):
    warga = get_object_or_404(Warga, id=warga_id)
    warga.delete()
    return redirect('daftar_warga')