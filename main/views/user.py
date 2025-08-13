from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import CreateView


class UserCreateView(CreateView):
    template_name = "auth/form.html"
    form_class = UserCreationForm
    success_url = "/auth/login"

class UserLoginView(LoginView):
    template_name = "auth/form.html"
    form_class = AuthenticationForm


<<<<<<< HEAD
class UserLogoutView(LogoutView):
    next_page = "/"
=======

>>>>>>> 9506b04264509a2dba462c66d3108557beaf5c7e
