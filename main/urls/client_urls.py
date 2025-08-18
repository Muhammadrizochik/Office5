from django.urls import path
from main.views import clients as views


urlpatterns = [
    path('clients', views.client_list, name='client_list'),
    path('clients/create/', views.client_create, name='client_create'),
    path('clients/update/<int:client_id>', views.client_update, name='client_update'),
    path('clients/<int:client_id>/delete/', views.client_delete, name='client_delete'),
]