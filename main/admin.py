from django.contrib import admin
from django.contrib.auth.models import User, Group
from main.models import clients, tasks

@admin.register(clients.Client)
class ClientsAdmin(admin.ModelAdmin):
    ...

@admin.register(tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'doer', 'client', 'added_at')
    list_filter = ('status', 'doer', 'client', 'added_at')
    search_fields = ('name', 'doer')
    ordering = ('-added_at',)