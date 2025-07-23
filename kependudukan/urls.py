from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_warga, name='daftar_warga'),

    path('tambah/', views.tambah_warga, name='tambah_warga'),
    path('ubah/<int:warga_id>/', views.ubah_warga, name='ubah_warga'),
    path('hapus/<int:warga_id>/', views.hapus_warga, name='hapus_warga'),
]

