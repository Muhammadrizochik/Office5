# from django.urls import path
# from main.views import home_view
# import main.views as views

from django.urls import path, include
from django.contrib import admin
from main.views import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]


