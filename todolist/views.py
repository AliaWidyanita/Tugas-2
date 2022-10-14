import datetime
from django.urls import reverse
from todolist.models import Task
from django.core import serializers
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse


@csrf_exempt
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todolist_data = Task.objects.filter(user=request.user)
    context = {
        'todolist_data': todolist_data,
        'user' : request.user
    }
    return render(request, "todolist_ajax.html", context)


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


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Task.objects.create(
            user = request.user,
            title = title,
            description = description,
        )
        return redirect('todolist:show_todolist')
    return render(request, 'create_task.html')


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url="/todolist/login/")
def task_status(request, id):
    task = Task.objects.get(id=id)
    task.is_finished = not task.is_finished
    task.save(update_fields=["is_finished"])
    return redirect('todolist:show_todolist')


@csrf_exempt
@login_required(login_url="/todolist/login/")
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('todolist:show_todolist')


def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@csrf_exempt
def add_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        todo = Task.objects.create(
            user = request.user,
            date = datetime.datetime.now(),
            title = title, 
            description = description,
            is_finished = False
        )
        context = {
            'pk': todo.pk,
            'fields': {
                'date': todo.date,
                'title': todo.title,
                'description': todo.description,
                'is_finished': todo.is_finished,
            }
        }
        return JsonResponse(context)