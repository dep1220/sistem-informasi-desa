from django.shortcuts import render
from kependudukan.models import Warga
from layanan_surat.models import PengajuanSurat
from django.db.models import Count
from django.contrib.auth.decorators import login_required


@login_required # 2. TAMBAHKAN DECORATOR INI
def dashboard_utama(request):
    # Menghitung statistik
    total_warga = Warga.objects.count()
    total_pengajuan = PengajuanSurat.objects.count()
    pengajuan_selesai = PengajuanSurat.objects.filter(status='Selesai').count()

    # Data untuk grafik jenis kelamin
    gender_data = Warga.objects.values('jenis_kelamin').annotate(jumlah=Count('jenis_kelamin'))

    konteks = {
        'total_warga': total_warga,
        'total_pengajuan': total_pengajuan,
        'pengajuan_selesai': pengajuan_selesai,
        'gender_data': list(gender_data) # Ubah ke list agar mudah dibaca JavaScript
    }
    return render(request, 'users/dashboard_utama.html', konteks)

