# **Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django**

**Nama   : Alia Widyanita Puspaningrum**

**NPM    : 2106751625**

**Kelas  : B**

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Asynchronous programming memiliki pendekatan pemrograman yang tidak terikat pada I/O Protocol. Pemrograman asynchronous tidak melakukan pekerjaannya dengan cara lama (eksekusi baris program satu persatu sesuai paradigma dan urutan program dalam kode). Asynchronous programming menjalankan program tanpa harus terikat dengan proses lain atau dapat disebut program berjalan secara independen.

Synchronous programming memiliki pendekatan pemrograman gaya lama. Program akan dieksekusi satu persatu sesuai dengan urutan dan prioritasnya. Hal ini memiliki kekurangan pada lama waktu eksekusi karena masing-masing pekerjaan harus menunggu pekerjaan lain selesai untuk diproses terlebih dahulu.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Event-driven adalah suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event yang merupakan keluaran atau tindakan pengguna, atau bisa berupa pesan dari program lainnya.

Penerapan paradigma tersebut dalam tugas ini contohnya adalah ketika pengguna menekan tombol "Create New Task", maka program akan menampilkan modal berisikan form. Lalu ketika pengguna mengisi form tersebut dan menekan tombol "Add Todo", maka program akan menambahkan data baru ke dalam Todolist sehingga Todolist saat ini bertambah sejumlah satu todo. Tombol yang diklik dalam alur tersebut disebut sebagai event.

## Jelaskan penerapan asynchronous programming pada AJAX.

1.  Tambahkan `<script>` yang memuat sebuah program JavaScript
2.  Tambahkan library AJAX berikut pada `<head>`
    ```
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    ```
3.  Tambahkan program AJAX di dalam tag tersebut seperti $.ajax({...}) sesuai dengan alur dan fitur program yang diinginkan
4.  Saat pengguna memiliki sebuah event atau permintaan ke server, maka event dari user ini akan diproses ke AJAX
5.  AJAX akan menampung semua event dari pengguna dan melakukan transfer data
6.  Data yang berasal dari pengguna kemudian diproses secara server-side dengan metode asynchronous
7.  Hasil dari proses data ini akan kemudian akan memperbarui halaman secara langsung
8.  Pengguna tidak perlu melakukan reload halaman, halaman telah terperbarui dengan data baru di dalamnya

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1.  Membuat view baru bernama show_json yang digunakan untuk mengembalikan seluruh data berupa json sesuai dengan filter `user=request.user` (user yang sedang login)
2.  Membuat path baru di dalam urls.py `/todolist/json` yang mengarah ke fungsi show_json dalam views.py
4.  Membuat template baru todolist_ajax.html untuk template yang menerapkan konsep AJAX dan mengarahkan url utama dari `/todolist` ke todolist_ajax.html
5.  Menambahkan library ajax yaitu `<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>` ke dalam head dari template
6.  Menambahkan AJAX GET ke alamat `/todolist/json` AJAX GET tersebut digunakan untuk mendapatkan data yang diperoleh dari json sesuai alamat tertera, data yang masuk akan diproses jika is_finished maka akan ditambahkan ke dalam container dengan id="todo-finish-card" jika sebaliknya akan ditambahkan ke dalam container dengan id="todo-unfinish-card"
7.  Membuat tombol "Add Task" yang membuka sebuah modal dengan form menambahkan task
8. Membuat view baru dalam views.py untuk menambahkan task baru ke dalam database. View yang saya buat bernama "add_todo" dengan csrf_exempt.
9.  Menambahkan path yang mengarah ke view add_todo yaitu `/todolist/add`
10. Menghubungkan form yang telah disusun ke path `/todolist/add`
11. Modal akan otomatis tertutup ketika user berhasil menambahkan todo
12. Membuat AJAX DELETE untuk tiap button delete pada setiap card yang ada dalam todolist. Jika user melakukan klik pada tag HTML (button delete) yang memiliki id="{todo.pk}-delete" secara dinamis maka card object dengan id="{todo.pk}" akan dihapus dari halaman
13. Membuat view dalam views.py yang mengarahkan penghapusan data dengan id tertentu
14. Membuat path /todolist/delete/{id} yang menerima ID dari path dan meneruskannya kepada view
15. Membuat fungsi JavaScript "deleteTodoCard" fungsi dapat dilihat di atas (digunakan untuk memanggil endpoint penghapusan task yaitu `/todolist/delete-task/${todo.pk}`)  