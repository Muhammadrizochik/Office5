from django.urls import path

import main.views.home as views

urlpatterns = [
    path("home", views.home, name=""),
]