from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from task_manager.users.forms import RegisterUserForm
from task_manager.mixins import (AuthorizationRequiredMixin,UserPermissionMixin,
                                 DeleteProtectionMixin)

from task_manager.tasks.models import TaskModel

# module with texts for buttons, flash messages, titles
from task_manager import texts


class UserListView(ListView):
    """
    URL ('/users/')
    Method GET Returns the HTML code of the user list page.
    """
    model = get_user_model()
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    extra_context = {
        'title': texts.USERS_LIST_TITLE_TEXT
    }


class RegisterUserView(SuccessMessageMixin, CreateView):
    """
    URL ('/users/create/')

    Method GET Returns the HTML code of the registration page.
    Method POST Creates a new user and redirects to the login page ('/login/')
    """
    form_class = RegisterUserForm
    template_name = 'users/update_register_user_form.html'
    success_url = reverse_lazy('login-page')
    extra_context = {
        'title': texts.SIGN_UP_TITLE_TEXT,
        'button_text': texts.SIGN_UP_BUTTON_TEXT
    }

    success_message = texts.REGISTER_USER_SUCCESS_MESSAGE


class UpdateUserView(AuthorizationRequiredMixin, UserPermissionMixin,
                     SuccessMessageMixin, UpdateView):
    """
    URL ('/users/<pk>/update/').

    Method GET Returns the HTML code of form with user data for editing
    Method POST Updates user data and redirects to the user list page
    """
    model = get_user_model()
    form_class = RegisterUserForm
    template_name = 'users/update_register_user_form.html'
    success_url = reverse_lazy('users-list-page')
    extra_context = {
        'title': texts.UPDATE_USER_TITLE_TEXT,
        'button_text': texts.EDIT_BUTTON_TEXT
    }

    permission_message = texts.PERMISSION_MESSAGE
    success_message = texts.UPDATE_USER_SUCCESS_MESSAGE


class DeleteUserView(AuthorizationRequiredMixin, UserPermissionMixin,
                     DeleteProtectionMixin, SuccessMessageMixin, DeleteView):
    """
    URL ('/users/<pk>/delete/').

    Method GET Returns the HTML code of the user deletion confirmation page
    Method POST delete user and redirects to the user list page
    """
    model = get_user_model()
    template_name = 'users/delete_user.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users-list-page')
    protected_url = reverse_lazy('users-list-page')
    extra_context = {
        'title': texts.DELETE_USER_TITLE_TEXT,
        'button_text': texts.DELETE_BUTTON_TEXT
    }

    permission_message = texts.PERMISSION_MESSAGE
    success_message = texts.DELETE_USER_SUCCESS_MESSAGE
    protected_message = texts.DELETE_USER_PROTECT_MESSAGE
