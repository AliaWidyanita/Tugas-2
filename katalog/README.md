# **PBP Tugas 2**

**Nama   : Alia Widyanita Puspaningrum**

**NPM    : 2106751625**

**Kelas  : B**



## Link Deploy Tugas 2 : 
**https://tugaspbp-alia.herokuapp.com/katalog/**

## Pertanyaan Tugas 2 : 
**1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html**
![GambarClientRequest-WebApplication]('../../ClientRequest-WebApplication.png?raw=true)

Pertama, permintaan yang masuk ke dalam server Django akan diproses melalui urls untuk diteruskan ke views yang didefinisikan oleh pengembang untuk memproses permintaan tersebut. Apabila terdapat proses yang membutuhkan keterlibatan database, maka nantinya views akan memanggil query ke models dan database akan mengembalikan hasil dari query tersebut ke views. Setelah permintaan telah selesai diproses, hasil proses tersebut akan dipetakan ke dalam HTML yang sudah didefinisikan sebelum akhirnya HTML tersebut dikembalikan ke pengguna sebagai respons.

**2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**

Virtual environment adalah sebuah alat untuk menjaga ruang terpisah untuk sebuah proyek dengan pustaka dan dependensi di satu tempat. Proyek tersebut mempunyai kebutuhan / dependent yang berbeda-beda antara satu dengan lainnya. Maka, dibutuhkanlah sebuah virtual environment untuk menjalankannya tanpa mengubah konfigurasi pada sistem operasi yang kita pakai. 

Ya, kita masih dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Terserah kita apakah menggunakan virtual environment di dalam repositori git lokal. Akan tetapi, kita harus menentukan file requirements.txt agar Heroku mengenal paket / dependensi Python apa yang harus diinstal. Namun, membuat requirements.txt akan sangat mudah dengan menggunakan virtual environment.

**3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.**

Pertama, saya menambahkan nama dan npm ke dalam list context pada file views.py dan juga menambahkan parameter context pada pengembalian fungsi render. 

Lalu saya mengubah Fill me! menjadi nama dan npm pada file HTML. Saya juga menambahkan semua barang dalam list barang seperti item_name, item_price, item_stock, rating, description, dan item_url. Saya lalu menambahkan agar link url dapat di klik dan merapihkan tabel agar lebih menarik dan enak di lihat. 

Terakhir, saya melakukan deployment ke Heroku. Pertama, saya membuat aplikasi baru pada Heroku. Setelah itu, saya menambahkan heroku API Key dan Heroku API Name ke Secrets -> Actions pada repositori GitHub. Akhirnya adalah membuka tab GitHub Actions dan menjalankan kembali workflow yang gagal.