# **PBP Tugas 3**

**Nama   : Alia Widyanita Puspaningrum**

**NPM    : 2106751625**

**Kelas  : B**


## Link Deploy Tugas 3 : 
🔗[**HTML**](https://tugaspbp-alia.herokuapp.com/mywatchlist/html)
🔗[**XML**](https://tugaspbp-alia.herokuapp.com/mywatchlist/xml)
🔗[**JSON**](https://tugaspbp-alia.herokuapp.com/mywatchlist/json)


## Pertanyaan Tugas 3 : 
**Jelaskan perbedaan antara JSON, XML, dan HTML!**

HTML dan XML merupakan bahasa mark up berdasarkan teks yang menggunakan penandaan. HTML digunakan untuk menyusun teks pada halaman web agar dirender dengan tepat di browser web. XML umumnya digunakan untuk menyusun data atau pesan. JSON digunakan untuk merepresentasikan data sebagai pasangan nilai kunci, yang dapat dengan mudah dikonversi ke dan dari objek JavaScript. Terdapat beberapa bagian yang membedakan ketiganya:

**Isi:** Informasi aktual yang perlu ditampilkan. Ini mengacu pada semua kata aktual yang membentuk dokumen dan yang juga menggambarkan beberapa jenis makna.

**Struktur:** Bagaimana semua informasi dalam dokumen diatur. Pada dasarnya ini adalah pemecahan konten menjadi informasi yang lebih kecil yang dapat dengan mudah dibaca atau diuraikan.

**Pemformatan:** Bagaimana dokumen ingin dimunculkan secara visual kepada seseorang yang membacanya.

**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

Aplikasi akan membutuhkan cara untuk menyimpan data yang telah di buat atau di peroleh ke dalam database. Hal ini dikarenakan adanya perubahan yang akan menyangkut data, contohnya seperti menyimpan atau mengirim data. HTML, XML, dan JSON berfungsi sebagai perantara pertukaran data antara back-end dengan front-end. _Data delivery_ membuat pengambilan data dari back-end dilakukan dengan lebih cepat dan pada akhirnya akan ditampilkan pada front-end.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

Pertama, saya membuat aplikasi baru bernama mywatchlist dengan menjalankan perintah python manage.py startapp mywatchlist di CMD. Aplikasi mywatchlist ditambahkan pada list INSTALLED_APPS pada folder project_django. Pada models.py di folder mywatchlist, ditambahkan atribut yang diinginkan, yaitu _watched_, _title_, _rating_, _release_ _date_, dan _review_. 

Setelah itu, membuat 10 data untuk objek yang sudah dibuat tadi pada file initial_mywatchlist_data.json di folder fixtures. Pada folder templates di file mywatchlist.html, membuat format HTML mengenai objek-objek yang sudah di buat pada folder fixtures. 

Selanjutnya, melakukan data delivery dengan mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format, yaitu HTML, XML, dan JSON. Dibuatlah sebuah _routing_ sehingga data yang sudah dibuat dapat di akses melalui URL yang diinginkan. 

Terakhir, saya melakukan deployment ke Heroku dengan menggunakan aplikasi yang telah dibuat pada Heroku untuk tugas sebelumnya.


## Screenshot URL - Postman Tugas 3 :
![ScreenshotPostman-HTML]('../../ScreenshotPostman-HTML.png?raw=true)
![ScreenshotPostman-XML]('../../ScreenshotPostman-XML.png?raw=true)
![ScreenshotPostman-JSON]('../../ScreenshotPostman-JSON.png?raw=true)