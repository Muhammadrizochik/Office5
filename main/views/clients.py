from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from models.clients import Client

@login_required
def client_list(request):
    if request.user.is_superuser:
        clients = Client.objects.all()
    else:
        clients = Client.objects.filter(created_by=request.user)
    return render(request, 'client_list.html', {'clients': clients})

@login_required
def client_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Client.objects.create(name=name, created_by=request.user)
        return redirect('client_list')
    return render(request, 'client_create.html')

@login_required
def client_update(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if client.created_by != request.user:
        return redirect('client_list')
    
    if request.method == "POST":
        client.name = request.POST.get('name')
        client.save()
        return redirect('client_list')
    
    return render(request, 'client_update.html', {'client': client})

@user_passes_test(lambda u: u.is_superuser)
@login_required
def client_delete(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.delete()
    return redirect('client_list')
