# **Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django**

**Nama   : Alia Widyanita Puspaningrum**

**NPM    : 2106751625**

**Kelas  : B**

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

_Asynchronous programming_ adalah program yang memiliki pendekatan yang tidak terikat pada _I/O Protocol_. Pemrograman asynchronous tidak mengeksekusi baris program satu persatu sesuai urutan program dalam kode. Metode pemrograman ini menjalankan program tanpa harus terikat dengan proses lain atau dapat berjalan dengan sendirinya (independen).

_Synchronous programming_ memiliki pendekatan yang mengeksekusi program satu persatu sesuai dengan urutan dan prioritasnya. Metode pemrograman ini memiliki kekurangan pada waktu eksekusi. Metode ini diharuskan untuk menunggu pekerjaan lain selesai diproses terlebih dahulu agar selanjutnya dapat berjalan.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

_Event-driven programming_ adalah suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event yang merupakan keluaran atau tindakan pengguna, atau bisa berupa pesan dari program lainnya.

Contoh dari paradigma ini adalah ketika pengguna menekan tombol, "Tugas Baru", maka program akan menampilkan modal form. Lalu, ketika pengguna mengisi form tersebut dan menekan tombol "Tambah Tugas", maka program akan menambahkan data baru ke dalam Todolist sehingga Todolist saat ini bertambah. Tombol yang diklik dalam alur tersebut disebut sebagai _event_.

## Jelaskan penerapan asynchronous programming pada AJAX.

AJAX atau _Asynchronous Javascript_ and XML adalah sekumpulan teknis pengembangan web. Saat _event_ sedang terjadi, hal tersebut akan mengakibatkan fungsionalitas dalam AJAX terjalankan. AJAX akan mengirimkan sebuah request ke server, dan melanjutkan eksekusi tanpa menunggu balasan dari server terlebih dahulu.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1.  Membuat view baru bernama `show_json` yang digunakan untuk mengembalikan seluruh data berupa json sesuai dengan user yang sedang login.
2.  Membuat path baru di dalam urls.py `/todolist/json` yang mengarah ke views.py fungsi `show_json`
3.  Membuat template baru todolist_ajax.html untuk template yang menerapkan konsep AJAX dan mengarahkan url utama dari `/todolist` ke html tersebut
4.  Menambahkan _library_ ajax yaitu `<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>` ke dalam _head_ todolist_ajax.html
5.  Menambahkan AJAX GET ke alamat `/todolist/json` yang digunakan untuk mendapatkan data dari json sesuai alamat yang tertera dan data yang masuk akan diproses
6.  Membuat tombol "Tugas Baru" yang membuka sebuah modal dengan form menambahkan task
7. Membuat view baru dalam views.py untuk menambahkan tugas baru ke dalam database
8.  Menambahkan path yang mengarah ke view `add_todo` dan menghubungkan form ke path `/todolist/add`
9. Page langsung _refresh_ ketika user menambahkan task
10. Membuat AJAX DELETE dengan membuat view dalam views.py yang menghapusankan data
11. Membuat path `/todolist/delete-task/{id}` yang menerima ID dari path dan meneruskannya ke view