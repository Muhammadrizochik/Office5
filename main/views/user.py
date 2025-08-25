from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.template.context_processors import request
from django.views.generic.edit import CreateView
from main.models.clients import User
from main.forms.users_form import UserUpdateForm


class UserCreateView(CreateView):
    template_name = "auth/form.html"
    form_class = UserCreationForm
    success_url = "/home"


class UserLoginView(LoginView):
    template_name = "auth/form.html"
    form_class = AuthenticationForm
    success_url = "/home"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


class UserLogoutView(LogoutView):
    next_page = "/"


@login_required
def user_list(request):
    if request.user.is_superuser:
        users = User.objects.all()
    else:
        users = User.objects.filter(created_by=request.user)
    return render(request, 'users/list.html', {'users': users})


@login_required
def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/users')
    else:
        form = UserUpdateForm(instance=user)

    return render(request, 'auth/form.html', {'form': form})


@login_required
def delete_user(request, pk):
    user = User.objects.filter(pk=pk)
    user.delete()
    return redirect("/users")