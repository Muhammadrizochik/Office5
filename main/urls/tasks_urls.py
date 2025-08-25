from django.urls import path
from main.views import tasks as views


urlpatterns = [
    path('tasks', views.tasks_list, name='tasks_list'),
    path('tasks/create/', views.tasks_create, name='tasks_create'),
    path('tasks/update/<int:tasks_id>', views.tasks_update, name='tasks_update'),
    path('tasks/<int:tasks_id>/delete/', views.tasks_delete, name='tasks_delete'),
]