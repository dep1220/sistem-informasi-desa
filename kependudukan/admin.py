from django.contrib import admin
from .models import Warga

# Register your models here.
@admin.register(Warga)
class WargaAdmin(admin.ModelAdmin):
    list_display = ('nik', 'nama_lengkap', 'jenis_kelamin', 'alamat', 'pekerjaan')
    search_fields = ('nik', 'nama_lengkap')