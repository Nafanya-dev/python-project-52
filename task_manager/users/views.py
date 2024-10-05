from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User
from task_manager.users.forms import RegisterUserForm

CHANGE_USER_ERROR_MESSAGE = _("You do not have permission"
                              "to change another user.")


class UserListView(ListView):
    """
    Handles requests to ('/users/')
    Method GET Returns the HTML code of the users list page.
    """
    model = get_user_model()
    template_name = 'users/user_list.html'
    context_object_name = 'users'


class RegisterUserView(CreateView):
    """
    Handles requests to ('/users/create/')

    Method GET Returns the HTML code of the registration page.
    Method POST Creates a new user and redirects to the login page ('/login/')
    """
    form_class = RegisterUserForm
    template_name = 'users/register_user.html'
    success_url = reverse_lazy('login-page')


class UpdateUserView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Handles requests to ('/users/<pk>/update/').

    If there is permission:
    Method GET Returns the HTML code of form with user data for editing
    Method POST Updates user data and redirects to the users list page

    If there is no permission:
    redirects to the users list page.
    show a message about no permission
    """
    form_class = RegisterUserForm
    template_name = 'users/update_user.html'
    success_url = reverse_lazy('users-list-page')
    login_url = reverse_lazy('login-page')

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('pk')
        return get_object_or_404(User, pk=user_id)

    def test_func(self):
        user_to_update = self.get_object()
        return self.request.user == user_to_update

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect(self.get_login_url())
        else:
            messages.error(self.request, CHANGE_USER_ERROR_MESSAGE)
            return redirect('users-list-page')


class DeleteUserView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Handles requests to ('/users/<pk>/delete/').

    If there is permission:
    Method GET Returns the HTML code of the user deletion confirmation page
    Method POST delete user and redirects to the users list page

    If there is no permission:
    redirects to the users list page.
    show a message about no permission
    """
    model = get_user_model()
    template_name = 'users/delete_user.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users-list-page')
    login_url = reverse_lazy('login-page')

    def test_func(self):
        user_to_delete = self.get_object()
        return self.request.user == user_to_delete

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect(self.get_login_url())
        else:
            messages.error(self.request, CHANGE_USER_ERROR_MESSAGE)
            return redirect('users-list-page')
