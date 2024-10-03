from django.urls import path

from task_manager.users import views


urlpatterns = [
    path('', views.UserListView.as_view(), name='users-list-page'),
    path('create/',
         views.RegisterUserView.as_view(),
         name='register-user-page'),
    path('<int:pk>/update/',
         views.UpdateUserView.as_view(),
         name='update-user-page'),
]
