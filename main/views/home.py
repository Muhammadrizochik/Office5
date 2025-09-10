from django.shortcuts import render, redirect
from django.db.models import Q

import main.models as models


def home(request):
    total_tasks = models.Tasks.objects.all().filter(Q(created_by=request.user) | Q(doer=request.user)).count()
    completed_tasks = models.Tasks.objects.all().filter(Q(status="tugallangan") & Q(doer=request.user)).count()
    in_progress_tasks = models.Tasks.objects.all().filter(Q(status="jarayyonda") & Q(doer=request.user)).count()
    new_tasks = models.Tasks.objects.all().filter(Q(status="yangi") &  Q(doer=request.user)).count()
    context = {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "in_progress_tasks": in_progress_tasks,
        "new_tasks": new_tasks,
    }
    return render(request, "index.html", context)
