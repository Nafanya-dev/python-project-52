from django.contrib import admin
from django.urls import path, include

from task_manager import views


urlpatterns = [
    path('', views.HomeView.as_view(), name="home-page"),

    path('users/', include('task_manager.users.urls')),

    path('statuses/', include('task_manager.statuses.urls')),

    path('tasks/', include('task_manager.tasks.urls')),

    path('labels/', include('task_manager.labels.urls')),

    path('login/',
         views.LoginUserView.as_view(),
         name='login-page'),

    path('logout/',
         views.LogoutUserView.as_view(),
         name='logout-page'),

    path('admin/', admin.site.urls),
]
