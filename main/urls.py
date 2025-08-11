

from django.urls import path
import main.views as views

urlpatterns = [
    path('home/', views.home_view, name='home')
]


