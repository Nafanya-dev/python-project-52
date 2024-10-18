from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.utils.enums import Template
from task_manager.mixins import (AuthorizationRequiredMixin,
                                 UserPermissionMixin, DeleteProtectionMixin)

from task_manager.users.forms import RegisterUserForm

# module containing the texts of common buttons and form titles
from task_manager import texts


USER_LIST_URL = reverse_lazy('user-list-page')

PERMISSION_MESSAGE = _("""You do not have permission to change another user.""")
REGISTER_USER_SUCCESS_MESSAGE = _("User successfully registered")
UPDATE_USER_SUCCESS_MESSAGE = _("User successfully changed")
DELETE_USER_SUCCESS_MESSAGE = _("User deleted successfully")
DELETE_USER_PROTECT_MESSAGE = _('Cannot delete user because it is in use')

USERS_LIST_TITLE_TEXT = _('Users')
SIGN_UP_TITLE_TEXT = _("Registration")
UPDATE_USER_TITLE_TEXT = _("Edit user")
DELETE_USER_TITLE_TEXT = _("Delete user")


class UserListView(ListView):
    """
    URL ('/users/')
    Method GET Returns the HTML code of the user list page.
    """
    model = get_user_model()
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    extra_context = {
        'title': USERS_LIST_TITLE_TEXT
    }


class RegisterUserView(SuccessMessageMixin, CreateView):
    """
    URL ('/users/create/')

    Method GET Returns the HTML code of the registration page.
    Method POST Creates a new user and redirects to the login page ('/login/')
    """
    form_class = RegisterUserForm
    template_name = Template.update_create.value
    extra_context = {
        'title': SIGN_UP_TITLE_TEXT,
        'button_text': texts.SIGN_UP_BUTTON_TEXT
    }

    success_url = reverse_lazy('login-page')

    success_message = REGISTER_USER_SUCCESS_MESSAGE


class UpdateUserView(AuthorizationRequiredMixin, UserPermissionMixin,
                     SuccessMessageMixin, UpdateView):
    """
    URL ('/users/<pk>/update/').

    Method GET Returns the HTML code of form with user data for editing
    Method POST Updates user data and redirects to the user list page
    """
    model = get_user_model()
    form_class = RegisterUserForm
    template_name = Template.update_create.value
    extra_context = {
        'title': UPDATE_USER_TITLE_TEXT,
        'button_text': texts.EDIT_BUTTON_TEXT
    }

    success_url = USER_LIST_URL

    permission_message = PERMISSION_MESSAGE
    success_message = UPDATE_USER_SUCCESS_MESSAGE


class DeleteUserView(AuthorizationRequiredMixin, UserPermissionMixin,
                     DeleteProtectionMixin, SuccessMessageMixin, DeleteView):
    """
    URL ('/users/<pk>/delete/').

    Method GET Returns the HTML code of the user deletion confirmation page
    Method POST delete user and redirects to the user list page
    """
    model = get_user_model()
    template_name = Template.delete.value
    context_object_name = 'object'
    extra_context = {
        'title': DELETE_USER_TITLE_TEXT,
        'button_text': texts.DELETE_BUTTON_TEXT,
    }

    success_url = USER_LIST_URL
    protected_url = USER_LIST_URL

    permission_message = PERMISSION_MESSAGE
    success_message = DELETE_USER_SUCCESS_MESSAGE
    protected_message = DELETE_USER_PROTECT_MESSAGE
