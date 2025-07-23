from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_utama, name='dashboard_utama'),
    # URL lain untuk users akan ditambahkan di sini nanti (login, logout, dll)
]