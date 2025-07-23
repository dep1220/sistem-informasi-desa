from django import forms
from .models import JenisSurat

class PengajuanSuratForm(forms.Form):
    jenis_surat = forms.ModelChoiceField(
        queryset=JenisSurat.objects.all(),
        empty_label="--- Pilih Jenis Surat ---",
        label="Jenis Surat yang Diajukan"
    )
    nik_pemohon = forms.CharField(
        label="NIK Pemohon",
        max_length=16,
        help_text="Pastikan NIK Anda sudah terdaftar di data kependudukan."
    )
    keperluan = forms.CharField(
        label="Keperluan",
        widget=forms.Textarea(attrs={'rows': 4})
    )