from django.urls import path

from task_manager.statuses import views


urlpatterns = [
    path('',
         views.StatusListView.as_view(),
         name='statuses-list-page'),
]
