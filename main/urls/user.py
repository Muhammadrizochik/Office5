from django.urls import path

import main.views.user as views

urlpatterns = [
    path('users', views.user_list, name='user_list'),
    path("", views.UserLoginView.as_view(), name="login"),
    path("logout", views.UserLogoutView.as_view(), name="logout"),
    path("create", views.UserCreateView.as_view(), name="create"),
]