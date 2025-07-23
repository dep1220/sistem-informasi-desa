from django.db import models

# Create your models here.
class Warga(models.Model):
    JENIS_KELAMIN_CHOICES = (
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    )


    nama_lengkap = models.CharField(max_length=255)
    nik = models.CharField(max_length=16, unique=True, help_text="Nomor Induk Kependudukan")
    jenis_kelamin = models.CharField(max_length=1, choices=JENIS_KELAMIN_CHOICES)
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    agama = models.CharField(max_length=50)
    pekerjaan = models.CharField(max_length=100)
    alamat = models.TextField()
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.nama_lengkap} ({self.nik})"
    
    class Meta:
        verbose_name = "Warga"
        verbose_name_plural = "Data Warga"
    
    