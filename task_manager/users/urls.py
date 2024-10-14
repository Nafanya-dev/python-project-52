from django.urls import path

from task_manager.users import views


urlpatterns = [
    # Users page. route('users/')
    path('', views.UserListView.as_view(),
         name='user-list-page'),

    # Route to create a user
    path('create/',
         views.RegisterUserView.as_view(),
         name='register-user-page'),

    # Route to update a user by their primary key (pk).
    path('<int:pk>/update/',
         views.UpdateUserView.as_view(),
         name='update-user-page'),

    # Route to delete a user by their primary key (pk).
    path('<int:pk>/delete/',
         views.DeleteUserView.as_view(),
         name='delete-user-page'),
]
