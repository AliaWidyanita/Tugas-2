from django.urls import path
from todolist.views import register, login_user, show_todolist, create_task, task_status, delete_task, logout_user, show_json, add_todo

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('create-task/', create_task, name='create_task'),
    path('task-status/<int:id>', task_status, name='task_status'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    path('logout/', logout_user, name='logout'),
    path('json/', show_json, name='show_json'),
    path('add/', add_todo, name="add_todo"),
]