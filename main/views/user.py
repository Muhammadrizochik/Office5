from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import CreateView


class UserCreateView(CreateView):
    template_name = "auth/form.html"
    form_class = UserCreationForm
    success_url = "/auth/login"


class UserLoginView(LoginView):
    template_name = "auth/form.html"
    form_class = AuthenticationForm


class UserLogoutView(LogoutView):
    next_page = "/"

