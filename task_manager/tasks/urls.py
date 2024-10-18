from django.urls import path

from task_manager.tasks import views


urlpatterns = [
    # Task list page. route('tasks/')
    path('', views.TaskListView.as_view(),
         name='task-list-page'),

    path('create/', views.CreateTaskView.as_view(),
         name='create-task-page'),

    path('<int:pk>/update/', views.UpdateTaskView.as_view(),
         name='update-task-page'),

    path('<int:pk>/delete/', views.DeleteTaskView.as_view(),
         name='delete-task-page'),

    path('<int:pk>/', views.TaskDetailView.as_view(),
         name='task-detail-page'),
]
