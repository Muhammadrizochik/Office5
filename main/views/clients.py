from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from main.models.clients import Client
from main.forms.clients_form import ClientForm

def client_list(request):
    search = request.GET.get("search")
    created_by = request.GET.get("created_by")

    clients = Client.objects.all()

    if search:
        clients = clients.filter(
            Q(f_name__icontains=search) | Q(phone__icontains=search)
        )
    if created_by:
        clients = clients.filter(created_by=created_by)

    context = {
        "clients": clients,
    }
    return render(request, "clients.html", context)


def client_create(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("client_list")
    else:
        form = ClientForm()
    return render(request, "create.html", {"form": form, "title": "Client qo‘shish"})


def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("client_list")
    else:
        form = ClientForm(instance=client)
    return render(request, "form.html", {"form": form, "title": "Clientni o‘zgartirish"})


def client_delete(request, pk):
    client = get_object_or_404(Client, client.id)
    if request.method == "POST":
        client.delete()
        return redirect("client_list")
    return render(request, "form.html", {"client": client})