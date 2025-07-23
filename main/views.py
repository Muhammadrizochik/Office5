from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Task
from .forms import TaskForm

def is_superuser(user):
    return user.is_superuser


@login_required
def task_list(request):
    if request.user.is_superuser:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(created_by=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.user != task.created_by and not request.user.is_superuser:
        return redirect('task_list')

    if request.method == 'POST':
        if request.user.is_superuser:
            form = TaskForm(request.POST, instance=task)
        else:
            form = TaskForm(request.POST, instance=task, fields=['status'])  # faqat status
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        if request.user.is_superuser:
            form = TaskForm(instance=task)
        else:
            form = TaskForm(instance=task, fields=['status'])
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
@user_passes_test(is_superuser)
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')

from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')


from django.shortcuts import render
from .models import Task

def tasks_list(request):
    name_filter = request.GET.get('name')
    doer_filter = request.GET.get('doer')
    status_filter = request.GET.get('status')

    tasks = Task.objects.all()

    if name_filter:
        tasks = tasks.filter(name__icontains=name_filter)
    if doer_filter:
        tasks = tasks.filter(doer__icontains=doer_filter)
    if status_filter:
        tasks = tasks.filter(status__iexact=status_filter)

    return render(request, 'task_list.html', {'tasks': tasks})
