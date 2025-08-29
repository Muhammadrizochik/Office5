from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from main.models.tasks import Tasks as Task, User
from main.forms.tasks_form import TaskAdminForm, TaskUpdateForm, TaskUpdateManagerForm

def is_superuser(user):
    return user.is_superuser


@login_required("")
def task_list(request):
    search = request.GET.get("search", "")
    created_by = request.GET.get("created_by", "")

    task = Task.objects.all()

    if search:
        task = task.filter(title__icontains=search)

    if created_by:
        task = task.filter(created_by=created_by)

    users = User.objects.all()

    return render(request, "task_list.html", {
        "task":task,
        "users": users
    })


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskAdminForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('/tasks')
    else:
        form = TaskAdminForm()
    return render(request, 'form.html', {'form': form, "title": "Task Create"})




@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        if request.user.is_superuser:
            form = TaskUpdateManagerForm(data=request.POST, instance=task)
        else:
            form = TaskUpdateForm(data=request.POST, instance=task)
        if not request.user.is_superuser:
            form.fields = {'status': form.fields['status']}
        if form.is_valid():
            form.save()
            return redirect('/tasks')
    else:
        if request.user.is_superuser:
            form = TaskUpdateManagerForm(instance=task)
        else:
            form = TaskUpdateForm(instance=task)
        if not request.user.is_superuser:
            form.fields = {'status': form.fields['status']}
    return render(request, 'form.html', {'form': form, "title": "Task Update"})


@login_required
@user_passes_test(is_superuser)
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('/tasks')

from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')


from django.shortcuts import render
from main.models.tasks import Tasks as Task

def task_filtered_list(request):
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
