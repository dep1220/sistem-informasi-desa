from django.urls import path
from . import views

urlpatterns = [
    path('ajukan/', views.ajukan_surat, name='ajukan_surat'),
    path('sukses/<uuid:kode_tracking>/', views.pengajuan_sukses, name='pengajuan_sukses'),
    path('lacak/', views.lacak_surat, name='lacak_surat'),
    path('dashboard/', views.dashboard_surat, name='dashboard_surat'),
    path('dashboard/proses/<int:pengajuan_id>/', views.proses_surat, name='proses_surat'),
    path('cetak/<int:pengajuan_id>/', views.cetak_surat, name='cetak_surat'),
]