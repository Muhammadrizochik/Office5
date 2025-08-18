from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import CreateView
from main.models.clients import User


class UserCreateView(CreateView):
    template_name = "auth/form.html"
    form_class = UserCreationForm
    success_url = "/auth/login"


class UserLoginView(LoginView):
    template_name = "auth/form.html"
    form_class = AuthenticationForm


class UserLogoutView(LogoutView):
    next_page = "/"


@login_required
def user_list(request):
    if request.user.is_superuser:
        users = User.objects.all()
    else:
        users = User.objects.filter(created_by=request.user)
    return render(request, 'users.html', {'users': users})
