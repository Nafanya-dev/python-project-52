"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from task_manager import views


urlpatterns = [
    # Main page
    path('', views.HomeView.as_view(), name="home-page"),

    # User list page
    path('users/', include('task_manager.users.urls')),

    # Status list page
    path('statuses/', include('task_manager.statuses.urls')),

    # Task list page
    path('tasks/', include('task_manager.tasks.urls')),

    # Label list page
    path('labels/', include('task_manager.labels.urls')),

    # Route for user login
    path('login/',
         views.LoginUserView.as_view(),
         name='login-page'),

    # Route for user logout
    path('logout/',
         views.LogoutUserView.as_view(),
         name='logout-page'),

    path('admin/', admin.site.urls),
]
