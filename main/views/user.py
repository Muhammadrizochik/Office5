from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

class UserLoginView(LoginView):
    template_name = "auth/form.html"
    form_class = AuthenticationForm