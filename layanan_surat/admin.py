from django.contrib import admin
from .models import JenisSurat, PengajuanSurat

class PengajuanSuratAdmin(admin.ModelAdmin):
    list_display = ('kode_tracking', 'pemohon', 'jenis_surat', 'status', 'tanggal_pengajuan')
    list_filter = ('status', 'jenis_surat')
    search_fields = ('pemohon__nama_lengkap', 'kode_tracking')

admin.site.register(JenisSurat)
admin.site.register(PengajuanSurat, PengajuanSuratAdmin)

