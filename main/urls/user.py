from django.urls import path

import main.views.user as views

urlpatterns = [
    path('users', views.user_list, name='user_list'),
    path('delete/', views.delete_user, name='delete_user'),
    path('users/update/<int:pk>', views.update_user, name='user_update'),
    path("", views.UserLoginView.as_view(), name="login"),
    path("logout", views.UserLogoutView.as_view(), name="logout"),
    path("create", views.UserCreateView.as_view(), name="create"),
]