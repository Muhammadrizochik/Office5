from django.contrib import admin
from django.contrib.auth.models import User, Group
from main.models import clients, tasks

@admin.register(clients.Client)
class ClientsAdmin(admin.ModelAdmin):
    ...

@admin.register(tasks.Tasks)
class TasksAdmin(admin.ModelAdmin):
    ...