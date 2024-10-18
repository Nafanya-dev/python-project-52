from django.urls import path

from task_manager.labels import views


urlpatterns = [
    # Label list page. route('labels/')
    path('', views.LabelListView.as_view(),
         name='label-list-page'),

    path('create/', views.CreateLabelView.as_view(),
         name='create-label-page'),

    path('<int:pk>/update/', views.UpdateLabelView.as_view(),
         name='update-label-page'),

    path('<int:pk>/delete/', views.DeleteLabelView.as_view(),
         name='delete-label-page'),
]
