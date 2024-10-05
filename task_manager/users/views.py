from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _

from task_manager.users.forms import RegisterUserForm
from task_manager.mixins import AuthorizationRequiredMixin, UserPermissionMixin


PERMISSION_MESSAGE = _("""You do not have permission
                       to change another user.""")

AUTHORIZATION_MESSAGE = _("You are not authorized! Please log in.")

REGISTER_USER_SUCCESS_MESSAGE = _("User successfully registered")
UPDATE_USER_SUCCESS_MESSAGE = _("User successfully changed")
DELETE_USER_SUCCESS_MESSAGE = _("User deleted successfully")


class UserListView(ListView):
    """
    URL ('/users/')
    Method GET Returns the HTML code of the users list page.
    """
    model = get_user_model()
    template_name = 'users/user_list.html'
    context_object_name = 'users'


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
        'title': _("Registration"),
        'button_text': _('Sign up')
    }

    success_message = REGISTER_USER_SUCCESS_MESSAGE


class UpdateUserView(AuthorizationRequiredMixin, UserPermissionMixin,
                     SuccessMessageMixin, UpdateView):
    """
    URL ('/users/<pk>/update/').

    Method GET Returns the HTML code of form with user data for editing
    Method POST Updates user data and redirects to the users list page
    """
    model = get_user_model()
    form_class = RegisterUserForm
    template_name = 'users/update_register_user_form.html'
    success_url = reverse_lazy('users-list-page')
    login_url = reverse_lazy('login-page')
    extra_context = {
        'title': _("Edit user"),
        'button_text': _('Edit')
    }

    authorization_message = AUTHORIZATION_MESSAGE
    permission_message = PERMISSION_MESSAGE
    success_message = UPDATE_USER_SUCCESS_MESSAGE


class DeleteUserView(AuthorizationRequiredMixin, UserPermissionMixin,
                     SuccessMessageMixin, DeleteView):
    """
    URL ('/users/<pk>/delete/').

    Method GET Returns the HTML code of the user deletion confirmation page
    Method POST delete user and redirects to the users list page
    """
    model = get_user_model()
    template_name = 'users/delete_user.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users-list-page')
    login_url = reverse_lazy('login-page')

    authorization_message = AUTHORIZATION_MESSAGE
    permission_message = PERMISSION_MESSAGE
    success_message = DELETE_USER_SUCCESS_MESSAGE
