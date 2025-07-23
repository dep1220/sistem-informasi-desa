from django.db import models

# Create your models here.
from django.db import models

class PotensiDesa(models.Model):
    KATEGORI_CHOICES = [
        ('Wisata', 'Wisata'),
        ('UMKM', 'UMKM'),
    ]
    nama = models.CharField(max_length=200)
    kategori = models.CharField(max_length=50, choices=KATEGORI_CHOICES)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='potensi_desa/')

    def __str__(self):
        return self.nama

class GaleriFoto(models.Model):
    keterangan = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='galeri/')

    def __str__(self):
        return self.keterangan
    
