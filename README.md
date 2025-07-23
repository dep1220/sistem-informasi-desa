# Sistem Informasi Desa Digital (SIDD)

Prototipe Sistem Informasi Desa Digital yang dibangun menggunakan Python dan Django untuk memenuhi kebutuhan digitalisasi desa di Kabupaten Katingan.

## Deskripsi Singkat

Sistem ini dirancang untuk membantu aparat desa dalam mengelola data kependudukan, menyediakan layanan publik secara online, dan mempromosikan potensi desa kepada masyarakat luas.

## Fitur Utama

-   **Dashboard Admin:**
    -   Login multi-peran (Kepala Desa, Sekretaris, Kaur).
    -   Statistik demografi penduduk dalam bentuk grafik.
    -   Manajemen data warga (Tambah, Lihat, Ubah, Hapus).
    -   Pengelolaan pengajuan surat dari warga.
-   **Portal Layanan Publik:**
    -   Formulir pengajuan surat online.
    -   Fitur pelacakan status pengajuan surat dengan kode unik.
    -   Tombol untuk mengunduh surat yang sudah jadi dalam format PDF.
-   **Profil Desa Publik:**
    -   Halaman utama yang menampilkan informasi desa.
    -   Galeri foto kegiatan dan potensi desa.
    -   Daftar potensi wisata dan UMKM.

## Teknologi yang Digunakan

-   **Backend:** Python, Django
-   **Frontend:** HTML, CSS, Bootstrap 5, Chart.js
-   **Database:** MySQL
-   **PDF Generation:** xhtml2pdf

## Cara Instalasi & Menjalankan Proyek

1.  **Clone repository ini:**
    ```bash
    git clone [https://github.com/namakamu/nama-repository.git](https://github.com/namakamu/nama-repository.git)
    cd nama-repository
    ```

2.  **Buat dan aktifkan virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Untuk Linux/Mac
    .\venv\Scripts\Activate.ps1 # Untuk Windows PowerShell
    ```

3.  **Install dependensi:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Catatan: Kamu perlu membuat file `requirements.txt` terlebih dahulu dengan perintah `pip freeze > requirements.txt`)*

4.  **Konfigurasi database** di `sistem_desa/settings.py`.

5.  **Jalankan migrasi:**
    ```bash
    python manage.py migrate
    ```

6.  **Buat superuser:**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Jalankan server:**
    ```bash
    python manage.py runserver
    ```
