from django.urls import path

from task_manager.tasks import views


urlpatterns = [
    path('', views.TaskListView.as_view(),
         name='task-list-page'),

    path('create/', views.CreateTaskView.as_view(),
         name='create-task-page'),
]
