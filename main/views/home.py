from django.shortcuts import render, redirect

import main.models as models


def home(request):
    total_tasks = models.Tasks.objects.all().filter(created_by=request.user).count()
    completed_tasks = models.Tasks.objects.all().filter(status="tugallangan", created_by=request.user).count()
    in_progress_tasks = models.Tasks.objects.all().filter(status="jarayyonda", created_by=request.user).count()
    new_tasks = models.Tasks.objects.all().filter(status="yangi", created_by=request.user).count()
    context = {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "in_progress_tasks": in_progress_tasks,
        "new_tasks": new_tasks,
    }
    return render(request, "index.html", context)
