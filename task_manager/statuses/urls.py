from django.urls import path

from task_manager.statuses import views


urlpatterns = [
    # Status list page. route('statuses/')
    path('',
         views.StatusListView.as_view(),
         name='status-list-page'),

    # Route to create a status
    path('create/',
         views.CreateStatusView.as_view(),
         name='create-status-page'),

    # Route to update a status by their primary key (pk).
    path('<int:pk>/update',
         views.UpdateStatusView.as_view(),
         name='update-status-page'),

    # Route to delete a status by their primary key (pk).
    path('<int:pk>/delete',
         views.DeleteStatusView.as_view(),
         name='delete-status-page')
]
