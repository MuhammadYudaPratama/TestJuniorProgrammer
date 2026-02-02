Aplikasi dikembangkan menggunakan Framework Django dan berfungsi untuk mengelola data produk, termasuk fitur CRUD, validasi form, serta filter produk berdasarkan status "bisa dijual".

- Buat & Aktifkan Virtual Environment
1. python -m venv venv
2. venv\Scripts\activate
- Install Dependency
1. pip install -r requirements.txt

- Migrasi Database
1. python manage.py makemigrations
2. python manage.py migrate

- Jalankan Server
1. python manage.py runserver

- Akses aplikasi di browser:
1. http://127.0.0.1:8000/

- Data Dummy (Pengganti API)
API Fastprint tidak dapat diakses karena masalah autentikasi (username & password).
Sebagai solusi, digunakan data dummy yang langsung disimpan ke database.

Data dummy digunakan agar:
Struktur database tetap sesuai soal
Fitur CRUD dapat diuji
Filter produk bisa dijalankan

Fitur Aplikasi
- Menampilkan Semua Produk

Menampilkan seluruh data produk dari database.
- Filter Produk "Bisa Dijual"

Menampilkan produk dengan status bisa dijual.
- Tambah Produk
1. Nama produk wajib diisi
2. Harga harus berupa angka
- Edit Produk
1. Data otomatis terisi
2. Validasi tetap diterapkan
- Hapus Produk
1. Dilengkapi konfirmasi JavaScript: return confirm("Yakin ingin menghapus produk ini?");
