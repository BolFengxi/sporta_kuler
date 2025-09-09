1. Mengimplementasikan checklist step-by-step
    - Mempersiapkan repository baru pada GitHub
    - Menyiapkan virtual environment pada terminal 
    - Menyiapkan folder proyek baru bernama "sporta_kuler" dan melakukan install dependencies serta inisiasi Django
    - Melakukan konfigurasi pada .env, .env.prod, serta settings.py
    - Mengunggah proyek ke repository GitHub dengan menambahkan .gitignore
    - Melakukan deployment melalui PWS dan menambahkan URL deployment pws
    - Membuat aplikasi main dalam proyek
    - Membuat model dengan nama porduct pada models.py dan menambahkan atributnya
    - Melakukan migrasi pada model yang baru dibuat 
    - Menghubungkan views.py dengan template
    - Melakukan routing URL aplikasi main

2. Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya
![bagan](image.png)

Penjelasan
User client mengirimkan request ke urls.py melalui browser dan mencocokkan URL dengan view yang sesuai. Setelah URL ditemukan, urls.py meneruskan request ke views.py. Setelah itu views.py menentukan apa yang akan dilakukan seperti mengambil data, proses data atau langsung menampilkan tampilan halaman. Jika membutuhkan data dari database, views.py akan meminta datanya dari models.py. Lalu dari views.py akan meneruskan data yang sudah didapat atau diproses ke html untuk ditampilkan ke user. Html akan mengirimkan response ke user client.

3. settings.py dalam proyek Django memiliki peran penting, yaitu tempat semua pengaturan global proyek Django. Pada settings.py tersimpan berbagai macam pengaturan seperti, penentuan database mana yang dipakai tergantung PRODUCTION, aplikasi mana yang aktif, file & template, siapa yang boleh mengakses, dan konfigurasi keamanan serta konfigurasi tambahaan dijalankan

4. Cara kerja migrasi database dalam Django
Setelah kita menambahkan atau mengubah isi dari model.py ktia akan melakukan migrasi model.
migrasi dilakukan dengan command "python manage.py makemigrations" dan "python manage.py migrate".
makemigrations menciptakan berkas yang berisi perubahan model yang belum diaplikasikan ke dalam basis data.
migrate mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke basis data. 

5. Menurut saya, kerangka kerja django terorganisasi dengan baik dan mudah untuk diinstall dan belajar. Arsitekturnya yang menggunakan MVT melatih pola pikir dalam software engineering.

6. Materi yang diberikan sudah baik dan lengkap.