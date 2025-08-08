from django.urls import path

import main.views.user as views

urlpatterns = [
    path("login", views.UserLoginView.as_view(), name="login"),
]