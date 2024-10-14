from django.urls import path

from task_manager.tasks import views


urlpatterns = [
    # Task list page. route('tasks/')
    path('', views.TaskListView.as_view(),
         name='task-list-page'),

    # Route to create a task
    path('create/', views.CreateTaskView.as_view(),
         name='create-task-page'),

    # Route to update a task by their primary key (pk).
    path('<int:pk>/update/', views.UpdateTaskView.as_view(),
         name='update-task-page'),

    # Route to delete a task by their primary key (pk).
    path('<int:pk>/delete/', views.DeleteTaskView.as_view(),
         name='delete-task-page'),

    # Task details page
    path('<int:pk>/', views.TaskDetailView.as_view(),
         name='task-detail-page'),
]
