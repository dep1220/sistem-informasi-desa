from xhtml2pdf import pisa
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import PengajuanSuratForm
from .models import PengajuanSurat, Warga
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

def ajukan_surat(request):
    if request.method == 'POST':
        form = PengajuanSuratForm(request.POST)
        if form.is_valid():
            try:
                # Cek apakah NIK pemohon ada di database Warga
                warga = Warga.objects.get(nik=form.cleaned_data['nik_pemohon'])
                
                # Buat objek pengajuan baru
                pengajuan = PengajuanSurat.objects.create(
                    jenis_surat=form.cleaned_data['jenis_surat'],
                    pemohon=warga,
                    keperluan=form.cleaned_data['keperluan']
                )
                # Arahkan ke halaman sukses dengan kode tracking
                return redirect('pengajuan_sukses', kode_tracking=pengajuan.kode_tracking)
            except Warga.DoesNotExist:
                # Jika NIK tidak ditemukan, tambahkan error ke form
                form.add_error('nik_pemohon', 'NIK tidak ditemukan di data kependudukan.')
    else:
        form = PengajuanSuratForm()
        
    return render(request, 'layanan_surat/form_pengajuan.html', {'form': form})

def pengajuan_sukses(request, kode_tracking):
    konteks = {
        'kode_tracking': kode_tracking,
    }
    return render(request, 'layanan_surat/pengajuan_sukses.html', konteks)


def lacak_surat(request):
    kode = request.GET.get('kode_tracking')
    pengajuan = None
    if kode:
        try:
            pengajuan = PengajuanSurat.objects.get(kode_tracking=kode)
        except PengajuanSurat.DoesNotExist:
            pengajuan = "Tidak Ditemukan"

    konteks = {
        'pengajuan': pengajuan,
    }
    return render(request, 'layanan_surat/hasil_pelacakan.html', konteks)



def dashboard_surat(request):
    semua_pengajuan = PengajuanSurat.objects.all().order_by('-tanggal_pengajuan')
    return render(request, 'layanan_surat/dashboard_surat.html', {'semua_pengajuan': semua_pengajuan})


# View BARU untuk memproses satu pengajuan
def proses_surat(request, pengajuan_id):
    pengajuan = get_object_or_404(PengajuanSurat, id=pengajuan_id)

    if request.method == 'POST':
        # Ambil status baru dari form yang dikirim
        status_baru = request.POST.get('status')
        if status_baru:
            pengajuan.status = status_baru
            pengajuan.save()
            return redirect('dashboard_surat')

    konteks = {
        'pengajuan': pengajuan
    }
    return render(request, 'layanan_surat/proses_surat.html', konteks)


def cetak_surat(request, pengajuan_id):
    pengajuan = get_object_or_404(PengajuanSurat, id=pengajuan_id)
    
    # Ambil template HTML
    template = get_template('layanan_surat/template_surat.html')
    konteks = {'pengajuan': pengajuan}
    html = template.render(konteks)
    
    # Buat file PDF di memori
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    
    # Jika tidak ada error, kembalikan response PDF
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename=surat_{pengajuan.pemohon.nik}.pdf'
        return response
    
    return HttpResponse("Error Saat Membuat PDF: <pre>%s</pre>" % pdf.err)

