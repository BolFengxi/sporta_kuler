TUGAS 2
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

TUGAS 3
1. Data delivery memastikan data yang benar, cepat dan aman sampai ke pengguna sehingga platform berguna dan dapat diandalkan

2. Perbedaan JSON dan XML
JSON : Lebih ringkas, struktur key:value bisa langsung dipetakan ke object, parsing umumnya lebih cepat, cocok untuk API
XML : Lebih kuat untuk dokumen markup, memiliki fitur-fitur untuk dokumen yang bersifat dokumen, lebih varbose 

Menurut saya lebih baik JSON tapi JSON dan XML tetap memiliki kelebihannya masing-masing
Alasan JSON lebih populer : Lebih ringan, native di js, parsing lebih sederhana, model datanya cocok untuk API

3. is_valid() adalah method pada instance Form atau ModelForm yang melakukan validasi field, digunakan untuk mencegah data yang tidak valid untuk masuk ke dalam database

4. Fungsi csrf_token adalah mengikat form ke sesi pengguna (atau ke cookie khusus) sehingga server dapat memverifikasi bahwa permintaan POST benar berasal dari halaman yang sah (origin yang benar). Django memeriksa token ini pada setiap request yang berpotensi mengubah state (POST, PUT, DELETE). Jika kita tidak menambahkan csrf_token maka Penyerang dapat memaksa user mengirim request berbahaya (misalnya mengubah data, menghapus resource, melakukan transaksi) dan tindakan yang memerlukan autentikasi bisa dieksekusi tanpa konfirmasi oleh user. Attacker akan memanfaatkan celah dengan cara Membuat halaman eksternal dengan form/action menuju target, otomatis submit via JavaScript untuk metode yang hanya butuh GET/POST sederhana, ini cukup berbahaya. Karena browser otomatis mengirim cookie sesi, server yang tidak mengecek CSRF akan menjalankan aksi.

5. Mengimplementasikan checklist step-by-step
    - Menambahkan beberapa kategori pada models.py 
    - Menambahkan views baru pada views.py : show_xml, show_json, show_xml_by_id, show_json_by_id
    - Menambahkan routing di urls.py ke masing-masing path baru untuk masing-masing view
    - Membuat templates html pada folder main yaitu untuk menampilkan list produk, add product, dan detail product
    - Membuat form tambah product dan membuat view untuk create_product
    - Membuat halaman detail product dan view show_product

6. Feedback untuk asdos, saya masih bingung terkait perbedaan pada data delivery dan bagaimana data dalam bentuk JSON dan XML ini dapat dimanfaatkan dan jika dimaanfaatkan untuk apa

7. Screnshoot 
![json](image-1.png)
![xml](image-2.png)
![jsonbyid](image-3.png)
![xmlbyid](image-4.png)


TUGAS 4
1. Mengimplementasikan checklist step-by-step
    - Membuat fungsi registrasi dengan menggunakan UserCreationForm pada views.py dan membuat template untuk register.
    - Membuat fungsi login menggunakan AuthenticationForm dan mengatur session agar hanya pengguna yang sudah login bisa mengakses halaman tertentu.
    - Membuat fungsi logout menggunakan logout(request) dan mengarahkan kembali ke halaman login.
    - Membuat dua akun pengguna dan menambahkan masing-masing tiga dummy data produk di lokal.
    - Menghubungkan model Product dengan User menggunakan ForeignKey agar data produk terasosiasi dengan pemiliknya.
    - Menampilkan detail informasi user yang sedang login (seperti username) di halaman utama.
    - Menerapkan cookies last_login untuk menyimpan kapan terakhir kali user login, lalu menampilkannya di halaman utama.
    - Melakukan add-commit-push ke GitHub dan deploy ke PWS.
2. AuthenticationForm adalah form bawaan Django untuk autentikasi user. Form ini digunakan untuk login dengan username dan password.

    - Kelebihan: Praktis karena sudah terintegrasi dengan sistem auth Django, aman karena otomatis memvalidasi password.
    - Kekurangan: Kurang fleksibel jika butuh kustomisasi field atau validasi tambahan.

3. Perbedaan autentikasi dan otorisasi

    - Autentikasi: proses memverifikasi identitas pengguna (contoh: login dengan username & password).
    - Otorisasi: proses memberikan hak akses tertentu pada user setelah autentikasi (contoh: admin boleh tambah produk, user biasa hanya bisa lihat produk).
    - Django: autentikasi dilakukan dengan AuthenticationForm, session, dan middleware bawaan. Otorisasi dilakukan dengan permissions, groups, dan decorator seperti @login_required atau @permission_required. 

4. Kelebihan dan kekurangan session & cookies dalam menyimpan state
- Session
Kelebihan : Lebih aman karena data tidak disimpan di browser, hanya ID session yang dikirim.
Kekurangan : Membutuhkan server-side storage sehingga menambah beban server.

-Cookies
Kelebihan : Tidak membebani server karena data disimpan di browser.
Kekurangan : Lebih rawan diubah user atau dicuri.

5. Apakah cookies aman secara default?
    Tidak sepenuhnya aman, ada risiko XSS dan session hijacking. Django menangani hal ini dengan:
    - Menggunakan flag HttpOnly agar cookie tidak bisa diakses lewat JavaScript.
    - Mendukung Secure flag agar cookie hanya dikirim lewat HTTPS.
    - Memberikan CSRF Token untuk mencegah serangan CSRF.

