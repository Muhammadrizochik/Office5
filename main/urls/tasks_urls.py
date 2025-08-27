from django.urls import path
import main.views.tasks as views


urlpatterns = [
    path('tasks', views.task_list, name='tasks_list'),
    path('tasks/create/', views.task_create, name='tasks_create'),
    path('tasks/update/<int:pk>', views.task_update, name='tasks_update'),
    path('tasks/delete/<int:pk>', views.task_delete, name='tasks_delete'),
]