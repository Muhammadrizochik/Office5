from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from main.models.clients import Client
from main.forms.clients_form import ClientForm
from django.contrib.auth.models import User

@login_required("")
def client_list(request):
    search = request.GET.get("search", "")
    created_by = request.GET.get("created_by", "")

    clients = Client.objects.all()

    if search:
        clients = clients.filter(f_name__icontains=search) | clients.filter(phone__icontains=search)

    if created_by:
        clients = clients.filter(created_by=created_by)

    users = User.objects.all()

    return render(request, "clients.html", {
        "clients": clients,
        "users": users
    })

def client_create(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("client_list")
    else:
        form = ClientForm()
    return render(request, "create.html", {"form": form, "title": "Client qo‘shish"})


def client_update(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == "POST":
        form = ClientForm(data=request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("client_list")
    else:
        form = ClientForm(instance=client)
    return render(request, "update.html", {"form": form, "title": "Clientni o‘zgartirish"})



@login_required
def client_delete(request, pk):
    client = Client.objects.filter(pk=pk)
    client.delete()
    return redirect('client_list')