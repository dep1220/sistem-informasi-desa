import uuid
from django.db import models
from kependudukan.models import Warga

class JenisSurat(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField(help_text="Deskripsi singkat atau persyaratan untuk surat ini.")
    
    def __str__(self):
        return self.nama

class PengajuanSurat(models.Model):
    STATUS_CHOICES = [
        ('Diajukan', 'Diajukan'),
        ('Diproses', 'Diproses'),
        ('Selesai', 'Selesai'),
        ('Ditolak', 'Ditolak'),
    ]

    kode_tracking = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    jenis_surat = models.ForeignKey(JenisSurat, on_delete=models.CASCADE)
    pemohon = models.ForeignKey(Warga, on_delete=models.CASCADE)
    keperluan = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Diajukan')
    tanggal_pengajuan = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.pemohon.nama_lengkap} - {self.jenis_surat.nama} ({self.status})"