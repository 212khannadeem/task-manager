from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('send_invitation/', views.send_invitation, name='send_invitation'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
]
