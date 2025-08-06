from django.urls import path
from main.views import home_view
import main.views as views

urlpatterns = [
    path('home/', views.home_view, name='home'),
]