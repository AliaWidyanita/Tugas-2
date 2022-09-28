# **Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django**

**Nama   : Alia Widyanita Puspaningrum**

**NPM    : 2106751625**

**Kelas  : B**

# Link Tugas 4

🔗[**ToDoList**](https://tugaspbp-alia.herokuapp.com/todolist/)
#

# Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

CSRF token atau _Cross Site Request Forgery_ token adalah sebuah tag yang dimiliki Django yang dapat diimplementasikan untuk menghindari serangan berbahaya. Tag ini berfungsi untuk mengatasi kemungkinan terjadinya serangan situs web. 

`{% csrf_token %}` menghasilkan token di sisi server saat merender halaman dan memastikan untuk memeriksa ulang token ini untuk setiap permintaan yang masuk kembali. 

Token CSRF mencegah CSRF karena tanpa token, penyerang tidak dapat membuat permintaan yang valid ke server backend. Selain itu, jika tidak ada `{% csrf_token %}` pada elemen `<form>`, maka permintaan tidak akan dieksekusi dan web akan menolak permintaan dengan mengeluarkan error.

# Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Kita tentu dapat membuat elemen `<form>` secara manual tanpa menggunakan generator seperti `{{ form.as_table }}`. Gambaran besar cara membuat `<form>` secara manual adalah sebagai berikut :

Pertama, kita dapat memanfaatkan tag `<form>` untuk membuat form di file HTML. Kedua, kita dapat menambahkan _action_ dan _method_ sebagai atribut. _Action_ memiliki peran sebagai pengiriman data form yang akan diproses dan _method_, yaitu "POST" atau "GET", memiliki peran untuk menjelaskan bagaimana data form akan dikirim oleh web. Ketiga, kita dapat menambahkan elemen input untuk keperluan form, di mana elemen-elemen input ini nantinya akan diisi oleh _user_. Terakhir, data yang diterima akan dicatat oleh form sehingga apabila _user_ melakukan _submit_ maka form akan dikirim sesuai dengan deklarasi action dan method yang sudah dilakukan sebelumnya.

# Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Pertama, input akan diminta dari user sesuai dengan form yang sudah di buat. Input tersebut akan dibawa oleh _request_ yang akan disimpan ke dalam variable oleh fungsi pada `views.py`. Setelah itu, program akan menginisiasi objek baru sesuai dengan _request_ atau input data dari _user_. Objek tersebut akan disimpan ke dalam database menggunakan perintah `<objek>.save()`. Selanjutnya, pengambilan objek dilakukan oleh `views.py` melalui `models.py` yang akan mengambil data yang sesuai dengan data user dari database. Terakhir, data yang tersimpan akan di-_render_ ke bentuk HTML untuk menampilkan halaman kepada _user_.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Pertama, membuat aplikasi django bernama `todolist` yang dapat dibuat dengan memasukkan command `python manage.py startapp todolist` ke _command promt_ pada direktori Tugas-PBP.

Kedua, path todolist dapat ditambahkan dengan memasukkannya ke urlpattern pada file `urls.py` yang berada pada folder `project-django`.

Ketiga, model Task dapat dibuat dengan membuat class dan atribut yang dibutuhkan dalam `models.py`. Atribut yang ditambahkan pada `models.py` di dalam folder `todolist` adalah _user_, _date_, _title_, _description_, dan _isfinished_. Setelah itu, menjalankan perintah `python manage.py makemigrations` untuk menyiapkan migrasi skema model ke dalam database Django lokal dan `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

Keempat, membuat fungsi `register`, `login_user`, dan `logout_user` pada file `views.py` yang menerima parameter request.

- Registrasi
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

- Login
```
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # melakukan login terlebih dahulu
            login(request, user) 
            # membuat response
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)
```

- Logout
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response
```

Kelima, membuat fungsi bernama `show_todolist`,  pada file `views.py` yang menerima parameter request. Selain itu, juga membuat halaman utama todolist pada file `todolist.html` di `templates`.

```
def show_todolist(request):
    todolist_data = Task.objects.filter(user=request.user)
    context = {
        'todolist_data': todolist_data,
        'user' : request.user
    }
    return render(request, "todolist.html", context)
```

Keenam, membuat fungsi bernama `create_task`,  pada file `views.py` yang menerima parameter request. Selain itu, juga membuat halaman untuk form create new task todolist pada file `create_task.html` di `templates`.

```
def create_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
        )
        return redirect('todolist:show_todolist')
    return render(request, 'create_task.html')
```

Ketujuh, membuat routing dengan menambahkan path ke urlpatterns pada `urls.py` sehingga fungsi `show_todolist`, `login_user`, `register`, `create_task`, `delete_task` dan `logout_user` dapat diakses.

```
urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('create-task/', create_task, name='create_task'),
    path('task-status/<int:id>', task_status, name='task_status'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    path('logout/', logout_user, name='logout'),
]
```

Kedelapan, melakukan add, commit, dan push ke repository github. Setelah itu, dapat langsung melakukan deploy ke Heroku karena menggunakan aplikasi Heroku yang sama dengan tugas sebelumnya. 

Kesembilan, membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.



Terakhir, mengimplementasikan fitur bonus. Pertama, membuat atribut is_finished pada model Task (dengan default value False). Fitur ini dilakukan dengan membuat dua kolom baru pada tabel task yang berisi status penyelesaian task dan tombol untuk mengubah status penyelesaian task tersebut. Selain itu, menambahkan kolom baru pada tabel task yang berisi tombol untuk menghapus suatu task.