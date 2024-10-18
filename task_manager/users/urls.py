from django.urls import path

from task_manager.users import views


urlpatterns = [
    # Users page. route('users/')
    path('', views.UserListView.as_view(),
         name='user-list-page'),

    path('create/',
         views.RegisterUserView.as_view(),
         name='register-user-page'),

    path('<int:pk>/update/',
         views.UpdateUserView.as_view(),
         name='update-user-page'),

    path('<int:pk>/delete/',
         views.DeleteUserView.as_view(),
         name='delete-user-page'),
]
