from django.urls import path
from main.views import clients as views



urlpatterns = [
    path('client_create', views.client_create),
    path('client_read', views.client_list),
    path('clients_update', views.client_update),
    path('client_delete', views.client_delete)
]

