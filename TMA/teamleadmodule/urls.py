from django.urls import path
from . import views

app_name = 'teamleadmodule'

urlpatterns = [
    path('taskpost/', views.taskpost, name='taskpost'),
    path('add_task_details/', views.add_task_details, name='add_task_details'),
    path('view/', views.view_task_details, name='view_task_details'),
]
