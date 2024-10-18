from django.urls import path

from task_manager.statuses import views


urlpatterns = [
    # Status list page. route('statuses/')
    path('',
         views.StatusListView.as_view(),
         name='status-list-page'),

    path('create/',
         views.CreateStatusView.as_view(),
         name='create-status-page'),

    path('<int:pk>/update/',
         views.UpdateStatusView.as_view(),
         name='update-status-page'),

    path('<int:pk>/delete/',
         views.DeleteStatusView.as_view(),
         name='delete-status-page')
]
